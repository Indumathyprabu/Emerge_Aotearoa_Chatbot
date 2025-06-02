import streamlit as st
import os
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()  # Load config.ini
        self.user_controls = {}

    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        # Default session state values
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            # Load LLM and Usecase options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                groq_key = st.text_input("Groq API Key", type="password")
                if groq_key:
                    st.session_state["GROQ_API_KEY"] = groq_key
                    self.user_controls["GROQ_API_KEY"] = groq_key
                else:
                    st.warning("⚠️ Please enter your Groq API key. https://console.groq.com/keys")

            # Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            # ✅ Tavily API prompt removed – no input or warning for it now

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        return self.user_controls
