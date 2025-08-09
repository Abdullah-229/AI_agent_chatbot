# streamlit_app.py

import streamlit as st
import requests

# Backend API URL
API_URL = "https://ai-agent-chatbot-ry1u.onrender.com/chat"

# Streamlit UI
st.set_page_config(page_title="LangGraph AI Agent", layout="centered")
st.title("🤖 LangGraph AI Agent Chatbot")

# Sidebar settings
st.sidebar.header("⚙️ AI Settings")
model_name = st.sidebar.selectbox("Select Model", ["llama3-70b-8192", "gpt-4o-mini"])
model_provider = st.sidebar.selectbox("Select Provider", ["Groq", "OpenAI"])
system_prompt = st.sidebar.text_area("System Prompt", "You are a helpful AI assistant.")
allow_search = st.sidebar.checkbox("Allow Web Search", value=True)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display immediately in UI
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare API payload
    payload = {
        "model_name": model_name,
        "model_provider": model_provider,
        "system_prompt": system_prompt,
        "messages": [m["content"] for m in st.session_state.messages if m["role"] == "user"],
        "allow_search": allow_search
    }

    try:
        # Call backend
        response = requests.post(API_URL, json=payload)
        response_data = response.json()

        # Extract AI reply
        ai_reply = response_data.get("reply", "No response from AI.")

        # Add AI reply to chat history
        st.session_state.messages.append({"role": "ai", "content": ai_reply})

        # Display AI reply
        with st.chat_message("ai"):
            st.markdown(ai_reply)

    except Exception as e:
        st.error(f"Error: {e}")
