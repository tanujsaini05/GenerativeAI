from key import gooogle_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain.prompts import ChatPromptTemplate

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    google_api_key=gooogle_api_key,  # Fixed variable name
    model="gemini-1.5-pro",
    temperature=0.2,
    #max_output_tokens=500,
    max_tokens = 500
)

# Correct prompt format
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot."),
    ("human", "Question: {question}")
])

# Output parser
output_parser = StrOutputParser()

# Correct chain order
chain = prompt | llm | output_parser

# Streamlit UI
st.title('Gemini ChatBot ☺')
input_ = st.text_input("Enter your question")

import asyncio

if input_:
    response = asyncio.run(chain.ainvoke({"question": input_}))  # Ensure async execution
    st.write(response)

