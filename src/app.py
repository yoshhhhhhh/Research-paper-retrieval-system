import re
import os
import streamlit as st
from whoosh.qparser import MultifieldParser, OrGroup
from whoosh.scoring import TF_IDF
from whoosh import scoring, index
import webbrowser
import time
INDEX_PATH = "./data/indexes"
TEXT_FOLDER = "./data/txt/"
PDF_FOLDER= "./data/pdf_downloads"

def submit_query(user_query, searcher, qp):
    user_query = user_query.lower()
    q = qp.parse(user_query)
    results = searcher.search(q, limit=10)
    ret = []
    for r in results:
        ret.append({"title": r["title"], "abstract": r["abstract"],  'score': r.score, 'rank': r.rank})
        
    return ret

def get_abstract_from_file(file_name):
    file_path = os.path.join(TEXT_FOLDER, f"{file_name}.txt")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            abstract = file.read()
        return abstract
    else:
        return None

def search_something():
    st.title("Research Paper Retrieval System")
    uin = st.text_input("Enter your query:")
    search_button = st.button("Search")
    if st.session_state.get('search_button') != True:
        st.session_state['search_button'] = search_button
        # st.snow()
        #st.balloons()

    if st.session_state['search_button'] == True:
        
        with st.spinner('Wait for it...'):
            time.sleep(1)
        

        ix = index.open_dir(INDEX_PATH)
        searcher = ix.searcher(weighting=scoring.BM25F(B=0.75, content_B=1.0, K1=1.2))
        #searcher = ix.searcher(weighting=TF_IDF())
        qp = MultifieldParser(["title", "abstract", "content"], schema=searcher.schema, group=OrGroup)

        ris = submit_query(uin, searcher, qp)
        sorted_ris = sorted(ris, key=lambda x: x["score"], reverse=True)
        st.success('Successfully retrieved', icon="✅")
        #st.snow()
        for w in sorted_ris:
            st.write(f"Paper: {w['title']}")
            abstract = get_abstract_from_file(w['title'])
            if abstract:
                st.write(f"Abstract: {abstract}")
            else:
                st.write("Abstract not found!")
            st.write(f"Score: {w['score']}")
            pdf_path = os.path.join(PDF_FOLDER, f"{w['title']}.pdf")
            if os.path.exists(pdf_path):
                if st.button(f"Paper: {w['title']}"):
                    st.write("Opening PDF...")
                    webbrowser.open(pdf_path)
            else:
                st.write("PDF not found!")

        user_query = uin.lower()
        q = qp.parse(user_query)
        corrected = searcher.correct_query(q, user_query)
        if corrected.query != q and len(sorted_ris) == 0:
            st.write(f"Did you mean: {corrected.string} ?")

        searcher.close()

if __name__ == '__main__':
    search_something()
