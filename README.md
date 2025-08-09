"# LangGraph AI Agent Chatbot 🤖

An intelligent chatbot system built with LangGraph, featuring a modern web interface and flexible AI model support. This project combines the power of various language models with web search capabilities to provide informative and context-aware responses.

## 🌟 Features

- **Multiple AI Model Support**
  - OpenAI GPT models
  - Groq-hosted models
  - Llama models
- **Web Search Integration**
  - Real-time web search capabilities
  - Context-aware responses
- **Modern User Interface**
  - Streamlit-based web interface
  - Chat history management
  - Real-time streaming responses
- **Customizable Settings**
  - Model selection
  - Provider selection
  - Custom system prompts
  - Toggleable web search

## 🛠️ Technical Architecture

The project follows a client-server architecture:

- **Frontend** (`frontend.py`)

  - Built with Streamlit
  - Real-time chat interface
  - Configurable settings sidebar
  - Session state management

- **Backend** (`backend.py`)

  - FastAPI server
  - RESTful API endpoints
  - Model management
  - Request validation

- **AI Agent** (`ai_agent1.py`)
  - LangGraph integration
  - Multi-model support
  - Web search capabilities
  - Response generation logic

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Abdullah-229/AI_agent_chatbot.git
   cd AI_agent_chatbot
   ```

2. Install dependencies:

   ```bash
   pipenv install
   ```

3. Set up environment variables:
   ```bash
   # Create a .env file with your API keys
   OPENAI_API_KEY=your_openai_key
   GROQ_API_KEY=your_groq_key
   TAVILY_API_KEY=your_tavily_key
   ```

### Running the Application

1. Start the backend server:

   ```bash
   pipenv run python backend.py
   ```

2. Launch the frontend:

   ```bash
   pipenv run streamlit run frontend.py
   ```

3. Access the application at `http://localhost:8501`

## 🔧 Configuration

- **Model Selection**: Choose between different AI models in the sidebar
- **Provider Selection**: Switch between OpenAI and Groq providers
- **System Prompt**: Customize the AI's behavior with system prompts
- **Web Search**: Toggle web search functionality

## 🚀 Deployment

The application can be deployed using Streamlit Cloud:

1. Push your code to GitHub
2. Connect your repository to Streamlit Cloud
3. Configure your environment variables in Streamlit Cloud's secrets management
4. Deploy!

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request"
