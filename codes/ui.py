import streamlit as st

def apply_custom_css():
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
                .stImage img {
            height: 150px !important;
            width: 150px !important;
            object-fit: cover !important;
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
        .header {
            display: flex;
            width: 100%;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            gap: 10px;
        }

        .header input {
            display: none; /* Hide the actual radio buttons */
        }

        .header label {
            flex: 1; /* Equal width */
            text-align: center;
            background-color: #333;
            color: white;
            padding: 15px;
            border-radius: 5px;
            cursor: pointer;
            border: 2px solid transparent;
            transition: background 0.3s, border 0.3s;
            font-size: 18px;
        }

        .header label:hover {
            background-color: #4d4d4d;
        }

        .header input:checked + label {
            background-color: #ffffff;
            color: black;
            border: 2px solid #ffffff;
        }
        .stButton button {
            width: 100%;
            height: 50px;
            font-size: 18px;
        }
        .stButton button.selected {
            background-color: #ffffff;
            color: black;
            border: 2px solid #ffffff;
        }
    </style>
    """, unsafe_allow_html=True)

def show_about_section():
    st.title("👨‍💻 About the Team Mates 👨‍💻")

    st.markdown("""
    <div style='height: px;'></div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        img_col, text_col = st.columns([1, 2])
        with img_col:
            st.image("/Users/shahnawazaadil/Desktop/Github/Gen-AI-With-Deep-Seek-R1/images/aadil.jpeg", caption="Shahnawaz Aadil", width=150)
        with text_col:
            st.markdown("""
            <div style="text-align: left;">
                <h2>Shahnawaz Aadil</h2>
                <p>CSE-Data Science Student</p>
                <p>shahnawazaadil7@gmail.com</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        img_col, text_col = st.columns([1, 2])
        with img_col:
            st.image("/Users/shahnawazaadil/Desktop/Github/Gen-AI-With-Deep-Seek-R1/images/salman.jpeg", caption="Mohammed Salman", width=150)
        with text_col:
            st.markdown("""
            <div style="text-align: left;">
                <h2>Mohammed Salman</h2>
                <p>CSE-Data Science Student</p>
                <p>mohammedsalman@gmail.com</p>
            </div>
            """, unsafe_allow_html=True)

    # Add custom CSS for fixed height and width with cropping
    st.markdown("""
    <style>
        .stImage img {
            height: 150px !important;
            width: 150px !important;
            object-fit: cover !important;
        }
    </style>
    """, unsafe_allow_html=True)

def show_header():
    if 'page' not in st.session_state:
        st.session_state.page = "General Chatbot"

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Chatbot", key="chatbot"):
            st.session_state.page = "General Chatbot"

    with col2:
        if st.button("Document Analysis", key="document_analysis"):
            st.session_state.page = "Document Analysis"

    with col3:
        if st.button("About", key="about"):
            st.session_state.page = "About"

    # Apply selected class to the active button using JavaScript
    '''st.markdown(f"""
    <style>
        .stButton button {{
            width: 100%;
            height: 50px;
            font-size: 18px;
        }}
        .stButton button.selected {{
            background-color: #ffffff;
            color: black;
            border: 2px solid #ffffff;
        }}
    </style>
    <script>
        const buttons = document.querySelectorAll('.stButton button');
        buttons.forEach(button => {{
            button.classList.remove('selected');
        }});
        const selectedButton = document.querySelector('.stButton button[data-baseweb="button"][key="{st.session_state.page.lower().replace(" ", "_")}"]');
        if (selectedButton) {{
            selectedButton.classList.add('selected');
        }}
    </script>
    """, unsafe_allow_html=True)'''