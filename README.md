# 🤖 LangChain Chatbot with OpenAI API

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)](#)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-orange)](#)

This repository contains my training exercise on building a **chatbot
application** using **LangChain**, **OpenAI API**, and **Streamlit**.\
The chatbot takes user input, processes it with LangChain's
`ChatPromptTemplate`, and generates responses using OpenAI's GPT model.

------------------------------------------------------------------------

## 📖 Contents

-   `app.py` -- Main application:
    -   Loads environment variables with `dotenv`
    -   Defines a chatbot prompt with `ChatPromptTemplate`
    -   Uses `ChatOpenAI` (GPT-3.5-turbo) for responses
    -   Chains the prompt → model → output parser
    -   Renders a **Streamlit** web UI for interaction
-   `requirements.txt` -- Required dependencies

------------------------------------------------------------------------

## 🚀 How to Use

### 1. Clone this repository

``` bash
git clone https://github.com/angseesiang/langchain-chatbot.git
cd langchain-chatbot
```

### 2. Create and activate a virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root and add the following
credentials:

    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key

> These keys are required to authenticate and enable the chatbot to
> interact with both **OpenAI's API** and **LangChain services**.

### 5. Launch the application

``` bash
streamlit run app.py
```

This command will start a **Streamlit web server** and open the chatbot
interface in your browser.

------------------------------------------------------------------------

## 🛠️ Requirements

See [`requirements.txt`](requirements.txt): - `langchain-openai` -
`langchain-core` - `python-dotenv` - `streamlit`

------------------------------------------------------------------------

## 📌 Notes

-   The chatbot currently uses **GPT-3.5-turbo** by default.
-   You can easily swap models by changing the `ChatOpenAI(model="...")`
    parameter in `app.py`.
-   This project was created during my **AI/ML training** to learn how
    to integrate LangChain with OpenAI and build a simple chatbot UI.

------------------------------------------------------------------------

## 📜 License

This repository is shared for **educational purposes**. Please credit if
you use it in your work.
