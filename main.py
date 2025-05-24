import streamlit as st
from ui import apply_custom_css, show_about_section, show_header
from chat import show_chatbot
from docu import show_document_analysis

st.set_page_config(layout="wide")

# Apply custom CSS
apply_custom_css()

# Initialize session state for page selection
if "page" not in st.session_state:
    st.session_state.page = "General Chatbot"

# Center the title and add a gap below it
st.markdown("""
    <h1 style='text-align: center;'>End to End GenAI Coding Assistant with DeepSeek-R1</h1>
    <div style='height: 20px;'></div>
    """, unsafe_allow_html=True)

# Show header with buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Chatbot"):
        st.session_state.page = "General Chatbot"
with col2:
    if st.button("Document Analysis"):
        st.session_state.page = "Document Analysis"
with col3:
    if st.button("About"):
        st.session_state.page = "About"

# Page selection based on button clicks
if st.session_state.page == "About":
    show_about_section()
elif st.session_state.page == "General Chatbot":
    show_chatbot()
elif st.session_state.page == "Document Analysis":
    show_document_analysis()