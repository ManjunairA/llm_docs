import json
import requests
from langchain_text_splitters import RecursiveJsonSplitter # type: ignore
# This is a large nested json object and will be loaded as a python dict
json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
splitter = RecursiveJsonSplitter(max_chunk_size=300)
# Recursively split json data - If you need to access/manipulate the smaller json chunks
json_chunks = splitter.split_json(json_data=json_data)
# The splitter can also output documents
docs = splitter.create_documents(texts=[json_data])

# or a list of strings
texts = splitter.split_text(json_data=json_data)

print(texts[0])
print(texts[1])