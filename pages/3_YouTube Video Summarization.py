
from dotenv import load_dotenv

load_dotenv("E:\PrivateFil\.env")  # take environment variables from .env.


import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
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

promptyt="""You are Youtube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 400 words. Please provide the summary of the text given here:  """


def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,promptyt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(promptyt+transcript_text)
    return response.text

st.title("Youtube Summarizer")



youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    # st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,promptyt)
        st.markdown("## Detailed Notes:")
        st.write(summary)