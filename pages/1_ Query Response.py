

from dotenv import load_dotenv

load_dotenv("E:\PrivateFil\.env")  # take environment variables from .env.


import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
# from langchain.chains import LLMChain
# from langchain import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi


def to_markdown(text):
    # Replace bullet points with markdown bullet points
    text = text.replace('•', '*')
    # Indent the text with markdown blockquote style
    text = textwrap.indent(text, '> ')
    # Display the text as markdown
    return st.markdown(text, unsafe_allow_html=True)

# added code till here

import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load geminiAI model and get respones

def get_gemini_response1(input,image):
    model1 = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response1 = model1.generate_content([input,image])
    else:
       response1 = model1.generate_content(image)
    return response1.text

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


##initialize our streamlit app



st.set_page_config(
    page_title=" Image with query",
   
)

st.title("Image & Query")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
# lan=st.text_input("Enter Language for Translation: (default language is English)",key="lan")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Search for Query")


if submit:
    if uploaded_file is None:
        response=get_gemini_response(f'Please provide a short and concise summary of the following speech:\n TEXT: {input}')
        # if lan!="":
        #     summary = text_summarization(response,lan)
        # else:
        #     summary = text_summarization(response,'English')

        st.subheader("The Response is")
        st.write(response)
    else:
        response1=get_gemini_response1(f'Please provide a short and concise summary of the following speech:\n TEXT: {input}',image)
        # if lan!="":
        #     summary1 = text_summarization(response1,lan)
        # else:
        #     summary1 = text_summarization(response1,'English')
        st.subheader("The Response is")
        st.write(response1)
