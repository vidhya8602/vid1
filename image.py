import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}
st.title("caption generation for image")
def query(filename):
    response = requests.post(API_URL, headers=headers, data=filename)
    return response.json()
url_input=st.text_input("enter the image")
bt=st.button("enter")
if bt and url_input:
    output=query(url_input)
    st.image(url_input)
    st.title(output[0]["generated_text"])
