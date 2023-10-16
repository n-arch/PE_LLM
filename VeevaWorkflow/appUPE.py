import streamlit as st
import json
import os

from models import upeEntry, guidelineAnswers

st.set_page_config(layout='wide')



# Create three columns for the chat interface with specified widths
col1, col2, col3 = st.columns(3)



# Add titles and text areas to each column
with col1:
    st.title("Title UPE")
    title_input = st.text_area("User Input", height=300, key="title_input")
    if st.button("Send"):
        response1 = upeEntry.title_prompt(title_input)
        st.text_area("Response", value=response1, height=300, key="response1")

with col2:
    st.title("Justification")
    chatgpt2_input = st.text_area("User Input", height=300, key="chatgpt2_input")
    if st.button("Send to ChatGPT-2"):
        response2 = upeEntry.justification_prompt(chatgpt2_input)
        st.text_area("Response", value=response2, height=300, key="response2")

with col3:
    st.title("GMP Check")
    chatgpt3_input = st.text_area("User Input", height=300, key="chatgpt3_input")
    if st.button("Send to ChatGPT-3"):
        response3 = guidelineAnswers.ask_guideline(chatgpt3_input)
        st.text_area("Response", value=response3, height=300, key="response3")
