import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLaMa 2 model

def getLLamaresponse(input_text,no_words,blog_style):
    llm = CTransformers(model="../chat LLaMa7b/llama-2-7b-chat.ggmlv3.q8_0.bin",
                 model_type ='llama',
                 config ={'max_new_tokens':256,
                          'temperature':0.01})
    tempelate="""
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """
    prompt =PromptTemplate(input_variables =['blog_style','input_text','no_words'],
                           template= tempelate)
    
    response =llm(prompt.format(blog_style= blog_style, input_text=input_text,no_words=no_words ))
    print(response)
    return response


st.set_page_config(page_title= "Generate Blogs",
                   page_icon=":bar_chart:",
                   layout ="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs :bar_chart:")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No. of Input')
with col2:
    blog_style= st.selectbox("Writing the blog for",
                             ('Researchers','Data Scientist','Common People'),
                             index =0)
    
submit= st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))

