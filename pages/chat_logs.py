# pages/1_📊_Chat_Logs.py
import streamlit as st
import pandas as pd
import json

# IMPORT THE DATABASE CONNECTION FROM OUR HELPER FILE
from utils.database import supabase

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")
st.title("📊 Patient Chat Analytics")
st.write("Monitor what patients are asking DentAI in real-time.")

# Fetch data from the chat_logs table
def fetch_chat_logs():
    response = supabase.table("chat_logs").select("*").execute()
    return response.data

data = fetch_chat_logs()

if data:
    df = pd.DataFrame(data)
    
    # --- CLEANUP CODE ---
    def get_text(raw_message):
        try:
            msg = json.loads(raw_message) if isinstance(raw_message, str) else raw_message
            return msg.get("content", "")
        except:
            return "Error parsing message"

    def get_sender(raw_message):
        try:
            msg = json.loads(raw_message) if isinstance(raw_message, str) else raw_message
            return msg.get("type", "unknown").capitalize() 
        except:
            return "Unknown"

    # Create clean columns
    df['Sender'] = df['message'].apply(get_sender)
    df['Clean Text'] = df['message'].apply(get_text)
    
    # Drop the ugly raw JSON column and reorder
    df = df.drop(columns=['message'])
    df = df[['id', 'session_id', 'Sender', 'Clean Text']]

    # --- DISPLAY METRICS ---
    total_patient_msgs = len(df[df['Sender'] == 'Human'])
    st.metric(label="Total Patient Questions Asked", value=total_patient_msgs)
    
    st.divider()

    # --- DISPLAY TABLE ---
    st.subheader("Raw Chat History")
    st.dataframe(df, width='stretch')

else:
    st.info("No chat logs found yet. Go send a message to your Telegram bot!")