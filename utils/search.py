import streamlit as st

def search(model, index, query):
    qe = model.encode(query).tolist()
    #Compute cosine similarity between query and embeddings vector.
    qs = index.query(qe, top_k = 10,
                        include_metadata = True)
    result = []
    for a in qs["matches"]:
        url = a['metadata']['url']
        result.append(url)
    
    return result

def display(urls):
    figures = []
    for url in urls:
        figures.append(f'''
        <figure style="margin : 5px !important;">
            <img src = "{url}" stylr="width:120px; height:90px">
        </figure>''')
    
    return st.markdown(f'''
        <div style="display: flex; flex-flow: row wrap; text-align: center"
        {''.join(figures)})
        >/div>
        ''',unsafe_allow_html = True)
    