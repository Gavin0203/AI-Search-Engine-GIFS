from os import urandom
from xml.etree.ElementInclude import include
from utils.vec_db import pinecone_init
from utils.retriever import retriever_init
from utils.search import display , search

import streamlit as st

retriever , embedding = retriever_init()
index = pinecone_init(api_k='2e0ab9ca-ec37-4e04-a822-be1aa31ed3c9',env='us-west1-gcp',index_name='gif-search',dimension=embedding,metric='cosine')

search(retriever,index,"dog smoking")