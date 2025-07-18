import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"  # Backend endpoint

st.set_page_config(
    page_title="🌍 Travel Planner Agentic Application",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Unique purple-blue theme styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e8eaed;
        min-height: 100vh;
    }
    
    .main-title {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #7c3aed 0%, #3b82f6 50%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .chat-header {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 1.3rem;
        font-weight: 500;
        color: #cbd5e1;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .chat-response {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        border: 1px solid rgba(124, 58, 237, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        line-height: 1.7;
        color: #f1f5f9;
    }
    
    .stTextInput > div > div > input {
        background: rgba(30, 41, 59, 0.7);
        color: #f1f5f9;
        border: 2px solid rgba(124, 58, 237, 0.4);
        border-radius: 12px;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 1.1rem;
        padding: 0.8rem 1rem;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #7c3aed;
        box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.2);
        background: rgba(30, 41, 59, 0.9);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #94a3b8;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #8b5cf6 100%);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 1rem 3rem;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover:before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #059669 0%, #2563eb 50%, #7c3aed 100%);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 12px 35px rgba(16, 185, 129, 0.6);
        border-color: rgba(255, 255, 255, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(1.02);
    }
    
    .stSpinner > div {
        border-top-color: #7c3aed !important;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        color: #fca5a5;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🌍 Travel Planner</h1>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown('<div class="chat-header">How can I help you plan your perfect trip?</div>', unsafe_allow_html=True)

# Chat input box
with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="e.g. Plan a trip to Goa for 5 days", label_visibility="collapsed")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        # Show thinking spinner
        with st.spinner("AI is thinking..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            # Display response in chat format
            st.markdown(f"""
            <div class="chat-response">
                <strong>🤖 AI Travel Assistant</strong><br>
                <small>Generated: {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')} | Created by: Nitesh Nepal</small>
                <hr style="border-color: #404040; margin: 1rem 0;">
                {answer}
                <hr style="border-color: #404040; margin: 1rem 0;">
                <small style="color: #888;">This travel plan was generated by AI. Please verify all information before your trip.</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Bot failed to respond: " + response.text)

    except Exception as e:
        st.error(f"❌ The response failed due to {e}")
