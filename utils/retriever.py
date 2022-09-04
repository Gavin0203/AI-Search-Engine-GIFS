from sentence_transformers import SentenceTransformer
import streamlit as st

@st.experimental_singleton
def retriever_init():
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings_no = model.get_sentence_embedding_dimension()

    return model, embeddings_no 