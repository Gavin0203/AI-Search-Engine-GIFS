import pinecone
import streamlit as st

#Connect to pinecone env
@st.experimental_singleton
def pinecone_init(api_k,env,index_name,dimension,metric):
    pinecone.init(
        api_key = api_k,  #app.pinecone.io
        environment = env
    )
    #index_name =  index_name         #'gif-search'
    #check if gif-search exists
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(
            index_name,
            dimension = dimension,  #Encoder o.p dimension.
            metric = metric #Should align with what the model is finetune to work with.
        )

    #Connecting to our new index.
    index = pinecone.Index(index_name)
    return index