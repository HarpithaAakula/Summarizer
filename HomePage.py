# Q&A Chatbot
#from langchain.llms import OpenAI

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Home Page")
st.sidebar.success("Select a page above.")

import streamlit as st


    

st.header('Page 1: Query Response')
st.write("""
This Page provides responses to queries, both with and without images, in English. 
Users can input their queries and choose whether to include an image or not.
- In this page:
    - You type your question (it can be about anything).
    - You can also include a picture if needed.
    - The system responds with helpful answers.
- Example: You could ask, "What's the weather today?" or "How do I bake a cake?".
""")

st.header('Page 2: Concise Summary in your Language')
st.write("""
This page provides a concise summary for queries in a specific language.
Users can input their queries in the specified language, and the app generates a summary.
- In this page:
    - You type your query and select the language you want the response in 
    - The app then creates a short summary of the answer for you.
- Example: If you ask, "What's the weather like today?" in Hindi, the app will respond for your query in Hindi
 
""")

st.header('Page 3: YouTube Video Summarization')
st.write("""
Page 3 is used for YouTube video summarization. 
Users need to provide the YouTube video link, and the app returns a detailed description.
- In this page:
    - You have to enter a link address of a YouTube video.
    - The tool watches writes a short description of what the video is about.
- Example: If you share a cooking video link, the tool might summarize it as "How to bake a cake."

""")




