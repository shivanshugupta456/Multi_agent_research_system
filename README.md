# Multi-Agent Research System

A sophisticated multi-agent research system built with **LangChain**, **LangGraph**, and **Streamlit**. This system leverages AI agents to conduct research, search the web, and provide intelligent responses using Mistral AI models.

## 🎯 Features

- **Multi-Agent Architecture**: Coordinated agents working together for research tasks
- **Web Search Integration**: Real-time web search using Tavily API
- **LLM-Powered**: Built on Mistral AI for intelligent reasoning
- **Pipeline Architecture**: Orchestrated workflow for complex tasks
- **Web Scraping**: Extract and process web content
- **Streamlit UI**: Beautiful, interactive web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Mistral API key
- Tavily API key (for web search)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Multi Agent System"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Add your API keys to `.env`:
   ```
   MISTRAL_API_KEY=your_mistral_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📁 Project Structure

```
.
├── app.py              # Streamlit UI and main application
├── agents.py           # Agent definitions and configurations
├── pipeline.py         # Research pipeline orchestration
├── tools.py            # Tool definitions for agents
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 Architecture

### Components

- **app.py**: Streamlit frontend with custom styling and user interface
- **agents.py**: Defines intelligent agents with specific roles and capabilities
- **pipeline.py**: Orchestrates the research workflow using LangGraph
- **tools.py**: Tools available to agents (search, scraping, etc.)

### Workflow

1. User submits a research query through the Streamlit interface
2. Pipeline routes the query to appropriate agents
3. Agents coordinate to:
   - Search the web using Tavily
   - Analyze and extract relevant information
   - Synthesize findings into a response
4. Results are presented to the user

## 📦 Dependencies

### Core Framework
- **langchain**: LLM orchestration framework
- **langgraph**: Graph-based agent orchestration
- **streamlit**: Web UI framework

### LLM & APIs
- **langchain-mistralai**: Mistral AI integration
- **tavily-python**: Web search API

### Utilities
- **python-dotenv**: Environment variable management
- **requests**: HTTP requests
- **beautifulsoup4**: Web scraping
- **pydantic**: Data validation
- **tenacity**: Retry handling
- **rich**: Enhanced terminal output

See [requirements.txt](requirements.txt) for complete list.

## 🔐 Security

⚠️ **Important**: Never commit `.env` files with API keys to version control. The `.gitignore` file is configured to prevent this.

Store sensitive information in environment variables:
- `MISTRAL_API_KEY`
- `TAVILY_API_KEY`

## 🛠️ Configuration

### Streamlit Configuration

The app includes custom CSS for a modern dark theme with:
- Space Grotesk and Space Mono fonts
- Custom color scheme (#0c0e14 background)
- Optimized layout

### LLM Settings

Configure agent models and parameters in `agents.py` based on your needs.

## 📝 Usage Examples

### Basic Research Query
```python
from pipeline import run_research_pipeline

result = await run_research_pipeline(query="Latest AI developments in 2024")
print(result)
```

### Custom Agent Configuration
Edit `agents.py` to customize agent behavior, system prompts, and capabilities.

## 🐛 Troubleshooting

### API Key Issues
- Ensure `.env` file exists in the project root
- Check that API keys are correct and have necessary permissions
- Verify keys are properly formatted

### Import Errors
```bash
# Reinstall dependencies
pip install --r requirements.txt --force-reinstall
```

### Streamlit Issues
```bash
# Clear cache and run
streamlit run app.py --logger.level=debug
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Create a feature branch
2. Make your changes
3. Submit a pull request

## 📄 License

This project is open source. Add your license information here.

## 📧 Contact

For questions or support, please create an issue in the repository.

---

**Built with ❤️ using LangChain, LangGraph, and Streamlit**
