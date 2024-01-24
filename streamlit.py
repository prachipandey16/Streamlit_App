import streamlit as st

pip install openai
import os
import openai
from openai import OpenAI

st.title("Text generation Using AI")
client = OpenAI(api_key='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')

def Messages(query):
    response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=query,
    temperature=0.7,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    #print(response)
    #if 'choices' in response: 
        #if (len(response.choices)>0):
    answer = response.choices[0].text
    return answer
    #print(answer)

query = st.text_input("Enter something in prompt : ")

if st.button("Get response"):
  response = Messages(query)
  st.text("Model response")
  st.write(response)
