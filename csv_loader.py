from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='C:/Users/Krishna/Desktop/langchain-prompts-main/Doc_Loader/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])