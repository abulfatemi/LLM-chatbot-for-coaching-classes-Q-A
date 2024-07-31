# -*- coding: utf-8 -*-
"""llm_abul_coaching

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fNTUO5FkldKD_wbnD2xya6SA-HQnokMA
"""


import key
Google_api_key=key.Google_api_key
from langchain_google_genai import GoogleGenerativeAI
llm=GoogleGenerativeAI(google_api_key=Google_api_key,model='gemini-1.5-flash')

from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS

instructor_embeddings=HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl')
vector_db_file_path='faiss_index'

def create_vector_db():
  loader=CSVLoader('abul_coaching_faqs.csv',source_column='prompt',encoding='latin-1')
  data = loader.load()
  vectordb=FAISS.from_documents(documents=data,embedding=instructor_embeddings)
  vectordb.save_local(vector_db_file_path)

if __name__=='__main__':
  create_vector_db()

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def get_qa_chain():
  vectordb=FAISS.load_local(vector_db_file_path,instructor_embeddings,allow_dangerous_deserialization=True)
  retriever=vectordb.as_retriever(score_threshold=0.7)
  prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""
  PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
  chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
  return chain