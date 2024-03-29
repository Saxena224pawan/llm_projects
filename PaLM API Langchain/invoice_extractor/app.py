from dotenv import load_dotenv
# Load enviroment variable from .env
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,prompt):
    response =model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into Bytes
        bytes_data  = uploaded_file.getvalue()
        
        images_parts =[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return images_parts
    else:
        FileNotFoundError()


# Initialie the streamlit app
st.set_page_config(page_title  ="MultiLanguage Invoice Extractor")

st.header('Gemini LLM Applications')

input = st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type =["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image, caption ="Uploaded Image.", use_column_width= True)
submit = st.button("Tell me about the image")

input_prompt="""
You are top-level expert in understanding invoices. We will upload an image as invoice 
and you will have to answer any question based on uploaded invoice image.
"""

if submit:
    images_data = input_image_setup(uploaded_file)

    response = get_gemini_response(input_prompt,images_data, input)
    st.subheader("The Response is")
    st.write(response)
