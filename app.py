import streamlit as st
import os
from dotenv import load_dotenv
import openai
from openai import AsyncOpenAI
import asyncio

# Load env variables
load_dotenv()

# Initialize client with API key from environment or user input
# The client will be re-initialized if the API key changes via user input
initial_api_key = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(api_key=initial_api_key or "")

st.set_page_config(page_title="🤖 OpenAI Q&A Chatbot", layout="wide")

st.title("🤖 OpenAI Q&A Chatbot")

# Custom CSS for a more professional look
st.markdown(
    """
    <style>
    .stApp { /* Main app container */
        background-color: #f0f2f6;
        color: #333333;
    }
    .st-emotion-cache-1c7y2kd { /* Sidebar background */
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    .st-emotion-cache-1c7y2kd .st-emotion-cache-10q70qd { /* Sidebar header */
        color: #1a1a1a;
    }
    .st-emotion-cache-1c7y2kd .stButton>button { /* Sidebar buttons */
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .st-emotion-cache-1c7y2kd .stButton>button:hover { /* Sidebar buttons hover */
        background-color: #45a049;
    }
    .st-emotion-cache-1r6y40z { /* Main content area */
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stTextArea>div>div>textarea { /* Text area styling */
        border-radius: 8px;
        border: 1px solid #cccccc;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button { /* Submit button styling */
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 25px;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover { /* Submit button hover */
        background-color: #0056b3;
    }
    .chat-message { /* Chat message container */
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .chat-message.user { /* User message specific styling */
        background-color: #d1e7dd;
        text-align: right;
    }
    .chat-message.ai { /* AI message specific styling */
        background-color: #e0f2f7;
        text-align: left;
    }
    .chat-message strong { /* Bold text in chat */
        color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Session state to store conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

def clear_chat():
    st.session_state.conversation = []
    st.rerun() # Rerun to clear display immediately

async def get_openai_response(prompt, model="gpt-3.5-turbo"):
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    api_key_input = st.text_input("Enter your OpenAI API Key:", type="password", value=initial_api_key)
    if api_key_input:

        client.api_key = api_key_input
    else:
        st.warning("Please enter your OpenAI API Key to use the chatbot.")

    model = st.selectbox("Choose model", options=["gpt-3.5-turbo", "gpt-4"], index=0)
    st.button("Clear Chat", on_click=clear_chat)

# Main content area
main_placeholder = st.empty()

with main_placeholder.container():
    # Display conversation history
    if st.session_state.conversation:
        st.markdown("### Conversation History")
        for i, chat in enumerate(st.session_state.conversation):
            st.markdown(f"<div class='chat-message user'><strong>Q:</strong> {chat['question']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-message ai'><strong>A:</strong> {chat['answer']}</div>", unsafe_allow_html=True)
            st.markdown("---", unsafe_allow_html=True)

    # User input at the bottom
    st.markdown("### Ask me anything:")
    user_question = st.text_area("Your Question:", height=100, key="user_input_area")

    submit = st.button("Submit")

    if submit and user_question and client.api_key:
        with st.spinner("Thinking..."):
            answer = asyncio.run(get_openai_response(user_question, model))
            # Save Q&A to conversation
            st.session_state.conversation.append({"question": user_question, "answer": answer})
        st.rerun() # Rerun to display new message
    elif submit and not client.api_key:
        st.error("Please enter your OpenAI API Key in the sidebar to submit your question.")
