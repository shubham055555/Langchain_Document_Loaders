from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 


loader = PyPDFLoader('C:/Users/Krishna/Desktop/langchain-prompts-main/Doc_Loader/dl-curriculum.pdf')

docs = loader.load()

print(docs)

print(type(docs))

print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)