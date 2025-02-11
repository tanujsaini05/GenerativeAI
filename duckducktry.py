from duckduckgo_search import DDGS
import streamlit as st


query = "Agents using langchain"
with DDGS() as ddgs:
    results = ddgs.news(query, max_results=5)

st.title("Try DuckDuckGo-Search")

def search_duckduckgo(query, num_results=5):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=num_results)
    return results
k = search_duckduckgo("Python programming")

for res in k:
    st.write(res["body"])
    st.write(res['href'])
#st.write(results)




