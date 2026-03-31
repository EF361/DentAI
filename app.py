import streamlit as st
from supabase import create_client, Client
import pandas as pd
import json

# Set up the page
st.set_page_config(page_title="DentAI Admin", layout="wide")
st.title("🦷 DentAI Analytics Dashboard")
st.write("Welcome to the control center. Here are the latest patient inquiries.")

# Connect to the Supabase "Visitor Logbook"
@st.cache_resource
def init_connection() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# Fetch data from the chat_logs table
def fetch_chat_logs():
    # Grab the data from Supabase
    response = supabase.table("chat_logs").select("*").execute()
    return response.data

# Display the data
data = fetch_chat_logs()

if data:
    df = pd.DataFrame(data)
    
    # --- NEW CLEANUP CODE STARTS HERE ---
    
    # 1. Create helper functions to extract the exact data we want
    def get_text(raw_message):
        try:
            # Check if it's a string, convert to dictionary
            msg = json.loads(raw_message) if isinstance(raw_message, str) else raw_message
            return msg.get("content", "")
        except:
            return "Error parsing message"

    def get_sender(raw_message):
        try:
            msg = json.loads(raw_message) if isinstance(raw_message, str) else raw_message
            # Capitalize 'human' to 'Human' and 'ai' to 'Ai'
            return msg.get("type", "unknown").capitalize() 
        except:
            return "Unknown"

    # 2. Create clean new columns
    df['Sender'] = df['message'].apply(get_sender)
    df['Clean Text'] = df['message'].apply(get_text)
    
    # 3. Drop the ugly raw JSON column
    df = df.drop(columns=['message'])
    
    # 4. Reorder the columns so it looks nice for the clinic staff
    # Make sure these column names match what your database actually outputs (e.g., 'id', 'session_id')
    df = df[['id', 'session_id', 'Sender', 'Clean Text']]
    
    # --- NEW CLEANUP CODE ENDS HERE ---

    st.subheader("Patient Chat History")
    st.dataframe(df, use_container_width=True)
    
    # Quick trick to count how many messages are from patients (Humans)
    total_patient_msgs = len(df[df['Sender'] == 'Human'])
    st.metric(label="Total Patient Questions Asked", value=total_patient_msgs)

else:
    st.info("No chat logs found yet. Go send a message to your Telegram bot!")