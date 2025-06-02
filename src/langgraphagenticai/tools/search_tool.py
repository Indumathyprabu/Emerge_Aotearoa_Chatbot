from langchain.tools import tool
from src.langgraphagenticai.vectorstore.vectorstore import VectorStore
import os

vectorstore = VectorStore()

# List of URLs to scrape for Emerge Aotearoa
EMERGE_URLS = [
    "https://emergeaotearoa.org.nz/",
    "https://emergeaotearoa.org.nz/about-us/",
    "https://emergeaotearoa.org.nz/our-services/",
    "https://emergeaotearoa.org.nz/mental-health/",
    "https://emergeaotearoa.org.nz/housing/",
    "https://emergeaotearoa.org.nz/youth-services/",
    "https://emergeaotearoa.org.nz/contact-us/",
    "https://emergeaotearoa.org.nz/careers/work-with-us/",    
    "https://emergeaotearoa.org.nz/news/",
    "https://emergeaotearoa.org.nz/events/",
    "https://emergeaotearoa.org.nz/our-people/",
    "https://emergeaotearoa.org.nz/our-partners/",
    "https://emergeaotearoa.org.nz/our-impact/",
    "https://emergeaotearoa.org.nz/annual-reports/",
    "https://emergeaotearoa.org.nz/our-values/",
    "https://emergeaotearoa.org.nz/our-history/",
    "https://emergeaotearoa.org.nz/our-board/",
    "https://emergeaotearoa.org.nz/our-leadership-team/"
    ]

@tool
def emerge_search_tool(query: str) -> str:
    """
    Searches the Emerge Aotearoa website for information using local vectorstore.
    """
    try:
        if not vectorstore.vectorstore:
            print("[INFO] Creating vectorstore...")
            vectorstore.create_vectorstore(EMERGE_URLS)

        results = vectorstore.search(query)
        if results:
            return "\n".join(results)
        else:
            return "❌ Sorry, I couldn't find relevant information in the site content."
    except Exception as e:
        return f"⚠️ Error during search: {e}"

def get_tools():
    """
    Return the list of tools to be used in the chatbot.
    """
    return [emerge_search_tool]

def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph.
    """
    from langgraph.prebuilt import ToolNode
    return ToolNode(tools=tools)
