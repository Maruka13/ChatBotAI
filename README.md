# 🤖 AI-Powered Customer Interaction Chatbot

This project is a high-performance, stateful chatbot built with Python and Streamlit, integrated with OpenAI’s GPT-4o model. It was designed to provide a seamless conversational experience by maintaining context throughout the session while following industry-standard security practices.

## 🛠️ Key Technical Features

### Stateful Conversation Management
Utilizes `st.session_state` to maintain a persistent chat history, enabling context-aware interactions across the entire session.

### Secure Credential Handling
Implements `python-dotenv` to manage API keys through environment variables, preventing sensitive data exposure in version control systems.

### Robust Data Pipeline
Optimized parsing of OpenAI Chat Completion response objects to ensure JSON-serializable payload handling and maintain application stability.

### Dynamic UI Rendering
Leverages Streamlit’s native chat components to create a clean, interactive, and professional conversational interface.

## 📚 Learning & Research

During the development of my first AI-driven system, I explored the Python ecosystem to understand which tools are best suited for different architectural scenarios.

### Web Frameworks & API Ecosystem

**Streamlit** was chosen for this project because it allows full frontend and backend development using only Python, with native Markdown support and rapid prototyping capabilities.

**Flask** and **FastAPI** were researched as lightweight and high-performance alternatives for building dedicated RESTful APIs.

**Django** was studied as a robust option for large-scale applications requiring built-in features such as an admin panel, authentication system, and ORM.

For AI ecosystem exploration, I analyzed **Hugging Face** and **Gradio** as alternatives for hosting and interacting with open-source machine learning models.

## 🧠 Streamlit Internal Logic

### Session State
Understood and implemented session persistence mechanisms to temporarily store chat history, allowing the system to “remember” previous interactions and maintain conversational continuity.

### UI Components
Mastered the use of `st.chat_message` to visually distinguish between user and assistant roles, enhancing clarity and user experience.

## 🚀 Engineering Challenges Solved

One critical technical challenge involved handling complex API response objects that were not directly JSON-serializable. Initially, this caused the following error:

TypeError: Object of type method is not JSON serializable

To resolve this, I implemented precise extraction logic using:

`response.choices[0].message.content`

This ensured proper isolation of the message payload, prevented serialization errors, and significantly improved overall system stability.

## 💻 Tech Stack

- Language: Python 3.13+
- Framework: Streamlit
- AI Engine: OpenAI GPT-4o API
- Environment Management: Dotenv (.env)

## 🔧 How to Run

1. Clone the repository.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Create a `.env` file and add your API key:
   `OPENAI_API_KEY=your_api_key_here`
4. Run the application:
   `streamlit run main.py`

## 📌 Project Goal

This project demonstrates secure API integration, stateful application architecture, clean UI development using a Python-only stack, and practical problem-solving when dealing with real-world API response handling. It represents a foundational step toward building scalable AI-powered applications.
