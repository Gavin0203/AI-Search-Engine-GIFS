# AI-Search-Engine-GIFS

This Repository contains the code to build a AI Search Engine using the power of NLP and Vector Databases.

## Pre-requisites

1. Knowledge on Text embeddings using Transfomers.
2. Sentence-Transformer library.
3. Setup Vector Database `Pinecone` and get the API to load the embeddings to the Vector DB.
4. Basic working of streamlit.

## Steps 

The steps followed to build the AI Based Search Engine for GIF's.

1. We first download the training data from ......
2. We then load the data, get the embeddings and update the embeddings and the metadata to the Pinecone vector DB.
3. We build a search engine layout using streamlit.
4. The user search query is then recorded and embedded and we find the most similar by using the Cosine Similarity metric.


<p align = "center">
<img src="https://github.com/pinecone-io/examples/blob/master/learn/projects/gif-search/assets/gif-search-0.png ">
</p>
