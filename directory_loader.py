from langchain_community.document_loaders import DirectoryLoader ,PyPDFLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 


loader = DirectoryLoader(
    path ='C:/Users/Krishna/Desktop/langchain-prompts-main/Doc_Loader/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader

)

docs = loader.load()



print(len(docs))

print(docs[326].page_content)
print(docs[326].metadata)