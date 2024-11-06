import streamlit as st
from googlesearch import search
from bs4 import BeautifulSoup
import requests

st.title("Search Anything 🔍")

def wikisearch(query):
    results = []
    for j in search(query, num=10, start=0, stop=10, pause=2.0):
        results.append(j)
    return results

query = st.text_input("Please enter your query:")
if query:
    results = wikisearch(query)
    for result in results:
        st.write(result)


if query:
    results = wikisearch(query)
    for result in results:
        response = requests.get(result)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else ""
        snippet = soup.find('meta', attrs={'name': 'description'})
        snippet = snippet['content'] if snippet else ""
        st.write(f"Title: {title}")
        st.write(f"Snippet: {snippet}")

