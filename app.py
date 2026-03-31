# app.py
import streamlit as st

st.set_page_config(page_title="DentAI System", page_icon="🦷", layout="centered")

st.title("🦷 Welcome to DentAI Core")
st.write("Please use the sidebar on the left to navigate to:")
st.markdown("""
- **📊 Chat Logs:** View patient conversations and analytics.
- **📄 Knowledge Base:** Upload, delete, and preview the clinic's dental guidelines.
""")    