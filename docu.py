import streamlit as st
import time
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import (
    PDFPlumberLoader,
    UnstructuredWordDocumentLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

def show_document_analysis():
    st.title("📘 DocuMind AI")
    st.markdown("### Your Intelligent Document Assistant")
    st.markdown("---")

    PROMPT_TEMPLATE = """
    You are a highly intelligent document assistant with expertise in summarization and reasoning.
    Use the provided context to answer concisely and factually.
    
    Question: {user_query}  
    Context: {document_context}  
    Additional Notes: If the context is insufficient, say "I don't know" instead of guessing.
    
    Answer:
    """

    STORAGE_PATH = '/Users/shahnawazaadil/Desktop/Github/Gen-AI-With-Deep-Seek-R1/documents/'
    EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
    DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
    LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

    def save_uploaded_file(uploaded_file):
        file_path = STORAGE_PATH + uploaded_file.name
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        return file_path

    def load_document(file_path):
        if file_path.endswith(".pdf"):
            loader = PDFPlumberLoader(file_path)
        elif file_path.endswith(".docx"):
            loader = UnstructuredWordDocumentLoader(file_path)
        elif file_path.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
        elif file_path.endswith(".csv"):
            loader = CSVLoader(file_path)
        elif file_path.endswith(".xlsx"):
            loader = UnstructuredExcelLoader(file_path)
        elif file_path.endswith(".pptx"):
            loader = UnstructuredPowerPointLoader(file_path)
        else:
            raise ValueError("Unsupported file type")
        return loader.load()

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
    uploaded_file = st.file_uploader(
        "Upload Document (PDF, DOCX, TXT, CSV, XLSX, or PPTX)",
        type=["pdf", "docx", "txt", "csv", "xlsx", "pptx"],
        help="Supported formats: .pdf, .docx, .txt, .csv, .xlsx, .pptx",
        accept_multiple_files=False
    )

    if uploaded_file:
        saved_path = save_uploaded_file(uploaded_file)
        raw_docs = load_document(saved_path)
        processed_chunks = chunk_documents(raw_docs)
        index_documents(processed_chunks)

        st.success("✅ Document processed successfully! Ask your questions below.")

        user_input = st.chat_input("Enter your question about the document...")

        if user_input:
            with st.chat_message("user"):
                st.write(user_input)

            with st.spinner("Analyzing document..."):
                relevant_docs = find_related_documents(user_input)
                ai_response = generate_answer(user_input, relevant_docs)

            with st.chat_message("assistant", avatar="🤖"):
                typing_placeholder = st.empty()
                simulate_typing(ai_response)

# Run the app
if __name__ == "__main__":
    show_document_analysis()