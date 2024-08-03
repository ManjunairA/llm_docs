from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain import hub
import os
from dotenv import load_dotenv, find_dotenv


# API set up
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_PROJECT'] = 'ret-rag'
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# Loading prompt
prompt = hub.pull("rlm/rag-prompt", api_url="https://api.hub.langchain.com")


# Loading data
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

# Split the data
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
splitted_text = text_splitter.split_documents(data)

# Embedding creation
model_name = "BAAI/bge-small-en"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
hf_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)

vector_store = Chroma.from_documents(splitted_text, hf_embeddings)

retriever = vector_store.as_retriever()

# Model loading
llm = ChatGroq(model="llama3-8b-8192", temperature=0)

# RetrievalQA
qa_chain = RetrievalQA.from_chain_type(llm, retriever = retriever, chain_type_kwargs = {"prompt" : prompt})


# Running chain
question = " What are the approcahes to do Task Decompositions? "
result = qa_chain({"query": question})

print(result["result"])

