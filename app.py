

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Hello! I am a chatbot. I am here to help you with any questions you have."),
        ("user","Question:{question}")
    ]
)

#streamlit framework

st.title("Chatbot")

st.title("Langchain with OpenAI API")
input_text = st.text_input("Enter your question here")

# openai LLM call

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

# chaining the prompt and the Llm
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

## chaining the prompt and the Llm
chain = prompt | llm | output_parser

if input_text:
    output = chain.invoke({'question': input_text})
    st.write(output)

