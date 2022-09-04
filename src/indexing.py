from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import sys
sys.path.append('./')

from utils.vec_db import pinecone_init
from utils.data import load_data

df = load_data("./TGIF-Release-master/data/tgif-v1.0.tsv",['url','description'])
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
model_dimension = model.get_sentence_embedding_dimension()
index = pinecone_init(api_k='<<Your API KEY>>',env='us-west1-gcp',index_name='gif-search',dimension=model_dimension,metric='cosine')

#Checking the embedding dimenstion, Important when initializing out Vector DB
print(model)

#Initializing the Retriver model.

batch_size = 64

for i in tqdm(range(0,len(df),batch_size)):
    i_end = min(i+batch_size, len(df))

    #extract batch
    batch = df.iloc[i:i_end]
    emb = model.encode(batch['description'].tolist()).tolist()
    #Get meta data
    meta = batch.to_dict(orient='records')  #{'description : "..." , 'url' : "..."}
    #create ids
    ids = [f"{idx}" for idx in range(i,i_end)]
    #add all  to upsert list
    to_upsert = list(zip(ids,emb,meta))
    #insert records to pinecone
    _ = index.upsert(vectors=to_upsert)

#Checking that we have all the vectors in index
print(index.describe_index_stats())