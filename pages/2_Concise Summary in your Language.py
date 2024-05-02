import streamlit as st 
from googletrans import Translator

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


languages = [
    "Afrikaans",
    "Akan",
    "Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Assamese",
    "Aymara",
    "Azerbaijani",
    "Bambara",
    "Bangla",
    "Basque",
    "Belarusian",
    "Bhojpuri",
    "Bosnian",
    "Bulgarian",
    "Burmese",
    "Catalan",
    "Cebuano",
    "Central Kurdish",
    "Chinese (Simplified)",
    "Chinese (Traditional)",
    "Corsican",
    "Croatian",
    "Czech",
    "Danish",
    "Divehi",
    "Dogri",
    "Dutch",
    "English",
    "Esperanto",
    "Estonian",
    "Ewe",
    "Filipino",
    "Finnish",
    "French",
    "Galician",
    "Ganda",
    "Georgian",
    "German",
    "Goan Konkani",
    "Greek",
    "Guarani",
    "Gujarati",
    "Haitian Creole",
    "Hausa",
    "Hawaiian",
    "Hebrew",
    "Hindi",
    "Hmong",
    "Hungarian",
    "Icelandic",
    "Igbo",
    "Iloko",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Javanese",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Kinyarwanda",
    "Korean",
    "Krio",
    "Kurdish",
    "Kyrgyz",
    "Lao",
    "Latin",
    "Latvian",
    "Lingala",
    "Lithuanian",
    "Luxembourgish",
    "Macedonian",
    "Maithili",
    "Malagasy",
    "Malay",
    "Malayalam",
    "Maltese",
    "Manipuri (Meitei Mayek)",
    "Māori",
    "Marathi",
    "Mizo",
    "Mongolian",
    "Nepali",
    "Northern Sotho",
    "Norwegian",
    "Nyanja",
    "Odia",
    "Oromo",
    "Pashto",
    "Persian",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Quechua",
    "Romanian",
    "Russian",
    "Samoan",
    "Sanskrit",
    "Scottish Gaelic",
    "Serbian",
    "Shona",
    "Sindhi",
    "Sinhala",
    "Slovak",
    "Slovenian",
    "Somali",
    "Southern Sotho",
    "Spanish",
    "Sundanese",
    "Swahili",
    "Swedish",
    "Tajik",
    "Tamil",
    "Tatar",
    "Telugu",
    "Thai",
    "Tigrinya",
    "Tsonga",
    "Turkish",
    "Turkmen",
    "Ukrainian",
    "Urdu",
    "Uyghur",
    "Uzbek",
    "Vietnamese",
    "Welsh",
    "Western Frisian",
    "Xhosa",
    "Yiddish",
    "Yoruba",
    "Zulu"
]

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

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


st.title("Language Translation")
input=st.text_input("Input Prompt: ",key="input")
    
target_language = st.selectbox("Select target language:", languages)
translate = st.button('Submit')
if translate:
    response1=get_gemini_response(f'Please provide a clear and concise summary of the following speech:\n TEXT: {input}')
    st.subheader(f'The Response is {target_language} is :')
    source_text = response1
    translator = Translator()
    out = translator.translate(source_text,dest=target_language)
    st.write(out.text)