from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 


load_dotenv()


model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4o-mini",
    temperature=0.3,
    
)

prompt = PromptTemplate(
    template='write a summary for the following poem -/n {poem} ',
    input_variables=['poem']
)

parser = StrOutputParser()


loader = TextLoader('C:/Users/Krishna/Desktop/langchain-prompts-main/Doc_Loader/cricket.txt', encoding= 'utf-8')

docs = loader.load()
print(type(docs))
print(len(docs))
print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model |parser
print(chain.invoke({'poem':docs[0].page_content}))

