
"""Json splittings"""
import json
import requests
from langchain_text_splitters import RecursiveJsonSplitter

json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
splitter = RecursiveJsonSplitter(max_chunk_size= 30)
json_chunks = splitter.split_json(json_data = json_data)
print(json_chunks[0])