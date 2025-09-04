# Drone Q&A Chatbot

A Streamlit app using LangChain and Ollama to answer drone-related questions.

## Setup

1. Install dependencies:
   ```bash
   pip install langchain-core langchain-community streamlit python-dotenv
   ```
2. Install Ollama and pull `llama2` model:
   ```bash
   ollama pull llama2
   ollama serve
   ```
3. Create `.env` file with:
   ```
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## Run

```bash
streamlit run ollama.py
```

## Usage

- Enter drone-related questions in the text input.
- Get answers powered by LangChain and Ollama's `llama2` model.