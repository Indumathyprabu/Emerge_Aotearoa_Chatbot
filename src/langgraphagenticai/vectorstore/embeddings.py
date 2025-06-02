from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

class Embeddings:
    def __init__(self):
        # Initialize the embedding model
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def embed_text(self, text: str):
        """
        Embeds the given text into vector representations.
        """
        return self.embedding_model.embed_query(text)

    def split_text(self, text: str, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Splits the text into chunks for embedding.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return text_splitter.split_text(text)