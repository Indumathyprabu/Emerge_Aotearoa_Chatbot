from langchain_community.vectorstores import FAISS
from .embeddings import Embeddings
from bs4 import BeautifulSoup
import requests

class VectorStore:
    def __init__(self):
        self.embeddings = Embeddings()
        self.vectorstore = None

    def scrape_website(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            for script in soup(["script", "style"]):
                script.decompose()
            content = soup.get_text(separator="\n", strip=True)
            return content.replace("\n\n", "\n").strip()
        except Exception as e:
            print(f"[ERROR] Failed to scrape {url}: {e}")
            return ""

    def create_vectorstore(self, urls: list):
        all_text = ""
        for url in urls:
            print(f"[INFO] Scraping: {url}")
            text = self.scrape_website(url)
            if text:
                all_text += text + "\n"

        if not all_text.strip():
            raise RuntimeError("No content scraped. Vector store creation aborted.")

        chunks = self.embeddings.split_text(all_text)
        self.vectorstore = FAISS.from_texts(chunks, self.embeddings.embedding_model)

    def search(self, query: str, k: int = 3):
        if not self.vectorstore:
            raise ValueError("Vector store not initialized. Call `create_vectorstore` first.")
        results = self.vectorstore.similarity_search(query, k=k)
        return [result.page_content for result in results]
