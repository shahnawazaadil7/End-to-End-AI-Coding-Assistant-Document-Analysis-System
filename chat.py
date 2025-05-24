import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
import time

def show_chatbot():
    st.title("🧠 GenAI Coding Assistant")
    st.caption("🚀 An Advanced AI Pair Programmer with Debugging Superpowers")

    # initiate the chat engine
    llm_engine = ChatOllama(
        model="deepseek-r1:1.5b",
        base_url="http://localhost:11434",
        temperature=0.3
    )

    # System prompt configuration
    system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant, highly skilled in Python, JavaScript, C++, and other programming languages. "
    "Your goal is to provide accurate, well-structured, and efficient solutions. "
    "For every coding question, follow these guidelines:\n"
    "- Provide **concise but clear** explanations before giving the solution.\n"
    "- **Break down complex concepts** into easy-to-understand steps.\n"
    "- Suggest **print statements and debugging strategies** when applicable.\n"
    "- Follow **best practices**, including code readability and efficiency.\n"
    "- **Ask for clarification** if the question is ambiguous.\n"
    "- Always respond in English.\n"
    "\nIf a user requests code, return it **formatted as a code block** (using triple backticks)."
    )

    # Session state management
    if "message_log" not in st.session_state:
        st.session_state.message_log = [{"role": "ai", "content": "Hi! How can I help you code today? 💻"}]
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
        think_placeholder = st.empty()  # Placeholder for <think><think> text
        final_placeholder = st.empty()  # Placeholder for actual AI response

        # Separate thinking text and actual response
        if "<think><think>" in text:
            thinking_text, actual_text = text.split("<think><think>", 1)
        else:
            thinking_text, actual_text = "", text  # No thinking text, just show actual output

        # Display the <think><think> part in a different color
        if thinking_text:
            think_placeholder.markdown(
                f'<span style="color: orange; font-weight: bold;">🤔 {thinking_text.strip()} </span>', 
                unsafe_allow_html=True
            )
            time.sleep(1)  # Pause for effect

        # Typing effect for actual output
        typing_text = ""
        for char in actual_text.strip():
            typing_text += char
            time.sleep(delay)
            final_placeholder.markdown(f'<span style="color: black;">{typing_text}</span>', unsafe_allow_html=True)

        # Clear the think text once the real response is fully typed
        time.sleep(0.5)
        think_placeholder.empty()

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