"""Document loaders with PDF, CSV, JSON, Webloader, text
with the version of langchain-community==0.2.10, langchain-core==0.2.23, langchain-ollama==0.1.0"""

# PDF Loader
from langchain_community.document_loaders import PyPDFLoader # type: ignore

pdf_loader = PyPDFLoader('your_document.pdf')
pages = pdf_loader.load_and_split()
#Page-wise print
print(pages[0])

##################################

# CSV Loader

from langchain_community.document_loaders import CSVLoader # type: ignore

csv_loader = CSVLoader('your_csvfile.csv')
csv_data = csv_loader.load()
# Row-wise print
print(csv_data[0])

########################################

from langchain.document_loaders import DirectoryLoader

loader =  DirectoryLoader('folder_name', glob='**/*.format(txt or pdf or etc)', loader_cls=TextLoader or PyPDFLoader or JSONLoader)
documents = loader.load()
print(documents)

########################################




# Json loader

from langchain_community.document_loaders import JSONLoader # type: ignore
import json
from pathlib import Path
from pprint import pprint

json_filepath = "your_json_data.json"
json_data = json.loads(Path(json_filepath).read_text())
pprint(json_data)

####################################################

# Web based loader

from langchain_community.document_loaders import WebBaseLoader # type: ignore

web_loader = WebBaseLoader("Web URL")

web_data = web_loader.load()
print(web_data)

#########################

#Text loading
from langchain_community.document_loaders import TextLoader # type: ignore

text_loader = TextLoader("your_text.txt")
text_data = text_loader.load()
print(text_data)