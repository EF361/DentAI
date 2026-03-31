# pages/2_📄_Knowledge_Base.py
import streamlit as st
import os
import base64

st.set_page_config(page_title="Knowledge Base", page_icon="📄", layout="wide")
st.title("📄 Knowledge Base Management")

# Ensure the upload directory exists
SAVE_DIR = "uploaded_pdfs"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Split the screen: Left (Controls), Right (Preview)
col_left, col_right = st.columns([1, 1])

# --- LEFT COLUMN: CRUD OPERATIONS ---
with col_left:
    st.subheader("1. Upload New Document")
    uploaded_file = st.file_uploader("Upload PDF Guidelines", type=["pdf"])
    
    if uploaded_file is not None:
        if st.button("Save Document to AI Memory"):
            # Save the file physically to the folder
            file_path = os.path.join(SAVE_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"✅ {uploaded_file.name} saved successfully!")
            # (Later, we will add the code here to send it to Supabase pgvector)

    st.divider()

    st.subheader("2. Manage Active Documents")
    # List all files currently in the folder
    saved_files = os.listdir(SAVE_DIR)
    
    if not saved_files:
        st.info("No documents uploaded yet.")
    else:
        # Create a dropdown to select a file
        selected_file = st.selectbox("Select a document to preview or delete:", saved_files)
        
        # Delete Button
        if st.button("🗑️ Delete Selected Document", type="primary"):
            os.remove(os.path.join(SAVE_DIR, selected_file))
            st.success(f"Deleted {selected_file}. Please refresh the page.")
            st.rerun()

# --- RIGHT COLUMN: LIVE PDF PREVIEW ---
with col_right:
    st.subheader("Live Document Preview")
    
    if saved_files and 'selected_file' in locals():
        file_path = os.path.join(SAVE_DIR, selected_file)
        
        # Read the PDF and convert it to base64 for the iframe
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
        # Display the PDF using HTML iframe
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.write("Select or upload a document to see the preview here.")