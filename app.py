from os import urandom
from xml.etree.ElementInclude import include
from utils.vec_db import pinecone_init
from utils.retriever import retriever_init
from utils.search import display

import streamlit as st

retriever , embedding = retriever_init()
index = pinecone_init(api_k='<<Your API KEY>>',env='us-west1-gcp',index_name='gif-search',dimension=embedding,metric='cosine')

st.write("""
## AI-Powered GIF Search""")

query = st.text_input("Enter search query","")

if query!="":
    with st.spinner(text="Searching... "):
        q = retriever.encode([query]).tolist()
        sim = index.query(q,top_k = 5, include_metadata=True)

        urls = []
        for res in sim['matches']:
            urls.append(res['metadata']['url'])
        
    with st.spinner(text="Fetching results"):
        display(urls)
