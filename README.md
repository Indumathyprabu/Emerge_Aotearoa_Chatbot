# 💬 Emerge Aotearoa Website Chatbot

A Streamlit-based chatbot application that answers questions based on **predefined URLs** from the [Emerge Aotearoa](https://www.emergeaotearoa.org.nz/) website. Built using **LangGraph**, **LangChain**, and **Streamlit**, this chatbot helps users navigate helpful information by fetching and summarizing data from the website's structured content.

---

## 🚀 Features

- 🌐 Answers based on hardcoded Emerge Aotearoa web pages  
- 🤖 Built using LangGraph and LangChain for modular agent flow  
- ⚙️ Streamlit UI for interaction  
- 🔐 Accepts Groq API key directly through the frontend  
- 🐳 Fully Dockerized — no manual setup needed!

---

## 📦 Requirements

- Docker installed ([Download Docker](https://www.docker.com/products/docker-desktop))  
- Git installed  

---

## 🧰 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emerge-chatbot.git
cd emerge-chatbot
```

### 2. Build the Docker image

```bash
docker build -t emerge-chatbot-app .
```

### 3. Run the Docker container

```bash
docker run -p 8501:8501 emerge-chatbot-app
```

### 4. Open in your browser

Go to: [http://localhost:8501](http://localhost:8501)

🔑 **Enter your Groq API Key** when prompted in the UI to use the chatbot.
