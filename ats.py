# Future work: Implement a more sophisticated ATS analyzer using advanced NLP techniques and machine learning models.


'''import streamlit as st
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_ollama import OllamaLLM
import base64
import io
from PIL import Image
import pdf2image
import time

def show_ats_analyzer():
    st.title("📄 ATS Resume Analyzer")
    st.markdown("### Optimize Your Resume for Job Applications")
    st.markdown("---")

    # Initialize models
    nlp = spacy.load("en_core_web_sm")
    language_model = OllamaLLM(model="deepseek-r1:1.5b")

    def extract_keywords(text):
        """Extracts keywords from the given text using spaCy."""
        doc = nlp(text)
        keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
        return keywords

    def calculate_ats_score(resume_text, job_description_text):
        """Calculates ATS score using cosine similarity."""
        resume_keywords = " ".join(extract_keywords(resume_text))
        job_description_keywords = " ".join(extract_keywords(job_description_text))
        vectorizer = CountVectorizer().fit_transform([resume_keywords, job_description_keywords])
        vectors = vectorizer.toarray()
        similarity = cosine_similarity(vectors)
        return round(similarity[0][1] * 100, 2)

    def generate_suggestions(resume_text, job_description_text):
        """Generates suggestions to improve the resume."""
        resume_keywords = set(extract_keywords(resume_text))
        job_description_keywords = set(extract_keywords(job_description_text))
        missing_keywords = job_description_keywords - resume_keywords
        if missing_keywords:
            return f"Consider adding these keywords to your resume: {', '.join(missing_keywords)}"
        else:
            return "Your resume already contains most of the relevant keywords."

    def input_pdf_setup(uploaded_file):
        """Convert the uploaded PDF to an image and prepare it for processing."""
        if uploaded_file is not None:
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts
        else:
            raise FileNotFoundError("No file uploaded")

    def get_deepseek_response(input_text, pdf_content, prompt):
        context = f"{input_text}\n\n{pdf_content[0]['data']}\n\n{prompt}"
        print("DEBUG: Context passed to DeepSeek model:", context)  # Debugging
        response = language_model.invoke(context)
        return response

    def simulate_typing(text, delay=0.001):
        typing_text = ""
        for char in text:
            typing_text += char
            time.sleep(delay)
            typing_placeholder.text(typing_text)

    # File Upload Section
    uploaded_resume = st.file_uploader("Upload Your Resume (PDF or Text)", type=["pdf", "txt"])
    job_description_text = st.text_area("Enter Job Description", placeholder="Paste the job description here...")

    submit1 = st.button("Tell Me About the Resume")
    submit3 = st.button("Percentage Match")

    input_prompt1 = """
    Your task is to evaluate the provided resume text against the given job description text.
    Use only the provided data and avoid making assumptions about the candidate's qualifications.
    """
    input_prompt3 = """
    You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
    Your task is to evaluate the resume against the provided job description. Provide the percentage match if the resume aligns 
    with the job description. First, output the percentage, then list the missing keywords, and finally provide your overall thoughts.
    """

    if uploaded_resume and job_description_text.strip():
        if uploaded_resume.type == "text/plain":
            resume_text = uploaded_resume.read().decode("utf-8")
        else:
            from PyPDF2 import PdfReader
            try:
                reader = PdfReader(uploaded_resume)
                resume_text = " ".join(page.extract_text() for page in reader.pages)
            except Exception as e:
                st.error(f"Error extracting text from PDF: {e}")
                resume_text = ""
        if not resume_text.strip():
            st.error("Failed to extract text from the uploaded resume. Please ensure the file is not empty or corrupted.")
        if submit1:
            pdf_content = input_pdf_setup(uploaded_resume)
            with st.spinner("Analyzing resume..."):
                response = get_deepseek_response(job_description_text, pdf_content, input_prompt1)
            with st.chat_message("assistant", avatar="🤖"):
                typing_placeholder = st.empty()
                simulate_typing(response)
        elif submit3:
            pdf_content = input_pdf_setup(uploaded_resume)
            with st.spinner("Calculating percentage match..."):
                response = get_deepseek_response(job_description_text, pdf_content, input_prompt3)
            with st.chat_message("assistant", avatar="🤖"):
                typing_placeholder = st.empty()
                simulate_typing(response)
    elif submit1 or submit3:
        st.write("Please upload the resume and enter the job description.")'''