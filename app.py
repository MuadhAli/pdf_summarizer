import streamlit as st
import os
import magic
import nltk
import tiktoken
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
os.environ['OPENAI_API_KEY'] = '....'




st.title("PDF Analyzer")


uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    loader = DirectoryLoader('./data/', glob='**/*.pdf')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
    docsearch = Chroma.from_documents(texts, embeddings)
    qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch)

    query = st.text_input("Enter your query", "")

    if st.button("Submit"):
        result = qa({"query": query})

        st.markdown('**Result:**')
        st.markdown(result['result'], unsafe_allow_html=True)

else:
    st.warning("Please upload a valid PDF file.")
