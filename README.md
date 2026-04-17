# SQL-Chatbot-Using-Langchain-and-Groq

# LangChain SQL Chatbot with Streamlit

An AI-powered conversational interface that lets you **chat with your SQL database** using natural language. Built with **LangChain**, **Groq LLM**, and **Streamlit**.

Ask questions like:
- "Show all students in Data Science section"
- "Who has the highest marks?"
- "List students with marks above 80 in DEVOPS"

The agent intelligently converts your question into SQL, executes it safely, and returns the results in a clean chat interface.

## Features

- Natural Language to SQL querying using LangChain SQL Agent
- Support for **SQLite** (local `student.db`) and **MySQL** databases
- Powered by **Groq** (fast inference with Llama model)
- Real-time visibility of agent's reasoning using Streamlit Callback Handler
- Persistent chat history in the session
- Secure database connection handling
- Sidebar options to switch between databases
- Caching of database connection for better performance

## Project Structure
├── app.py                 # Main Streamlit application
├── sqlite.py              # Script to create and populate student.db
├── student.db             # SQLite database file
├── requirements.txt       # Python dependencies
└── README.md

## Tech Stack

- **Streamlit** – Web UI
- **LangChain** – Agent framework & SQL Toolkit
- **Python** - Backend
- **Groq** – LLM (meta-llama/llama-4-scout-17b-16e-instruct)
- **SQLAlchemy** – Database engine
- **SQLite** + **MySQL** support

## How to Use

1. Add your Groq API Key in the sidebar.
2. Choose the database:
  - Use SQLITE 3 Database- Student.db (default, local)
  - Connect to your SQL Database (MySQL – enter host, user, password, db name)
3. Start chatting with the database in natural language.
