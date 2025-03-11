import streamlit as st
from langchain_ollama import ChatOllama, OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
import time

# Custom CSS styling
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    .stSelectbox svg {
        fill: white !important;
    }
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    .card {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .card img {
        border-radius: 50%;
        width: 150px;
        height: 150px;
    }
    .card h2 {
        color: #ffffff;
    }
    .card p {
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# About section
if st.button("About"):
    with st.expander("About the Project Mates", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="card">
                <img src="/Users/shahnawazaadil/Desktop/Github/Gen-AI-With-Deep-Seek-R1/images/1702675497539.jpeg" alt="Shahnawaz Aadil">
                <h2>Shahnawaz Aadil</h2>
                <p>CSE-Data Science Student</p>
                <p>Passionate about AI and Machine Learning</p>
                <p>Contact: shahnawazaadil7@gmail.com</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
                <img src="/Users/shahnawazaadil/Desktop/Github/Gen-AI-With-Deep-Seek-R1/images/1702675497539.jpeg" alt="Teammate Name">
                <h2>Teammate Name</h2>
                <p>Teammate's Role</p>
                <p>Teammate's Interests</p>
                <p>Contact: teammate_email@example.com</p>
            </div>
            """, unsafe_allow_html=True)

# Page selection
page = st.selectbox("Select a page", ["General Chatbot", "Document Analysis"])

if page == "General Chatbot":
    st.title("🧠 GenAI Chatbot for College Major Project")
    st.caption("🚀 An Advanced AI Pair Programmer with Debugging Superpowers")

    # initiate the chat engine
    llm_engine = ChatOllama(
        model="deepseek-r1:1.5b",
        base_url="http://localhost:11434",
        temperature=0.3
    )

    # System prompt configuration
    system_prompt = SystemMessagePromptTemplate.from_template(
        "You are an expert AI coding assistant. Provide concise, correct solutions "
        "with strategic print statements for debugging. Always respond in English."
    )

    # Session state management
    if "message_log" not in st.session_state:
        st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
        st.session_state.greeting_sent = True

    # Chat container
    chat_container = st.container()

    # Display chat messages
    with chat_container:
        for message in st.session_state.message_log:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input and processing
    user_query = st.chat_input("Type your coding question here...")

    def generate_ai_response(prompt_chain):
        processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
        return processing_pipeline.invoke({})

    def build_prompt_chain():
        prompt_sequence = [system_prompt]
        for msg in st.session_state.message_log:
            content = msg["content"].replace("{", "{{").replace("}", "}}")
            if msg["role"] == "user":
                prompt_sequence.append(HumanMessagePromptTemplate.from_template(content))
            elif msg["role"] == "ai":
                prompt_sequence.append(AIMessagePromptTemplate.from_template(content))
        return ChatPromptTemplate.from_messages(prompt_sequence)

    def simulate_typing(text, delay=0.001):
        typing_text = ""
        for char in text:
            typing_text += char
            time.sleep(delay)
            typing_placeholder.text(typing_text)

    if user_query:
        # Add user message to log and display it immediately
        st.session_state.message_log.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)
        
        # Generate AI response with live thinking
        with st.spinner("🧠 Processing..."):
            prompt_chain = build_prompt_chain()
            thinking_placeholder = st.empty()
            for i in range(5):  # Simulate thinking process
                time.sleep(0.5)
            ai_response = generate_ai_response(prompt_chain)
            thinking_placeholder.empty()
        
        # Add AI response to log with typing effect
        st.session_state.message_log.append({"role": "ai", "content": ai_response})
        typing_placeholder = st.empty()
        simulate_typing(ai_response)
        
        # Rerun to update chat display
        st.rerun()

elif page == "Document Analysis":
    st.title("📘 DocuMind AI")
    st.markdown("### Your Intelligent Document Assistant")
    st.markdown("---")

    PROMPT_TEMPLATE = """
    You are an expert research assistant. Use the provided context to answer the query. 
    If unsure, state that you don't know. Be concise and factual (max 3 sentences).

    Query: {user_query} 
    Context: {document_context} 
    Answer:
    """
    PDF_STORAGE_PATH = '/Users/shahnawazaadil/Desktop/Github/Gen-AI-With-Deep-Seek-R1/documents'
    EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
    DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
    LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

    def save_uploaded_file(uploaded_file):
        file_path = PDF_STORAGE_PATH + uploaded_file.name
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        return file_path

    def load_pdf_documents(file_path):
        document_loader = PDFPlumberLoader(file_path)
        return document_loader.load()

    def chunk_documents(raw_documents):
        text_processor = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        return text_processor.split_documents(raw_documents)

    def index_documents(document_chunks):
        DOCUMENT_VECTOR_DB.add_documents(document_chunks)

    def find_related_documents(query):
        return DOCUMENT_VECTOR_DB.similarity_search(query)

    def generate_answer(user_query, context_documents):
        context_text = "\n\n".join([doc.page_content for doc in context_documents])
        conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        response_chain = conversation_prompt | LANGUAGE_MODEL
        return response_chain.invoke({"user_query": user_query, "document_context": context_text})

    def simulate_typing(text, delay=0.001):
        typing_text = ""
        for char in text:
            typing_text += char
            time.sleep(delay)
            typing_placeholder.text(typing_text)

    # File Upload Section
    uploaded_pdf = st.file_uploader(
        "Upload Research Document (PDF)",
        type="pdf",
        help="Select a PDF document for analysis",
        accept_multiple_files=False
    )

    if uploaded_pdf:
        saved_path = save_uploaded_file(uploaded_pdf)
        raw_docs = load_pdf_documents(saved_path)
        processed_chunks = chunk_documents(raw_docs)
        index_documents(processed_chunks)
        
        st.success("✅ Document processed successfully! Ask your questions below.")
        
        user_input = st.chat_input("Enter your question about the document...")

        if user_input:
            # Display user question immediately
            with st.chat_message("user"):
                st.write(user_input)
            
            with st.spinner("Analyzing document..."):
                relevant_docs = find_related_documents(user_input)
                ai_response = generate_answer(user_input, relevant_docs)
            
            # Add AI response to log with typing effect
            typing_placeholder = st.empty()
            simulate_typing(ai_response)
            
            with st.chat_message("assistant", avatar="🤖"):
                st.write(ai_response)