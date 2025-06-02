import os
import sys

# ✅ Suppress Streamlit errors due to PyTorch internals

os.environ["STREAMLIT_TELEMETRY_ENABLED"] = "false"




# Apply nest_asyncio before launching the app
import nest_asyncio
nest_asyncio.apply()

# 🔁 Your actual Streamlit app logic
from src.langgraphagenticai.main import load_langgraph_agenticai_app

if __name__ == "__main__":
    load_langgraph_agenticai_app()
