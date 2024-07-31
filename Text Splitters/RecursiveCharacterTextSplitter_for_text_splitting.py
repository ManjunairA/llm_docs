"""Text loading and splitting the text."""
from langchain_text_splitters import RecursiveCharacterTextSplitter # type: ignore
from langchain_community.document_loaders import TextLoader # type: ignore

text_loader = TextLoader("git_instruction.txt")
text_data = text_loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=6,
    chunk_overlap=2)

texts = text_splitter.split_documents(text_data)
print(texts)