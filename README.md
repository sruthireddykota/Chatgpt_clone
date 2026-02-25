#  YouTube Script Writing Tool

An AI-powered Streamlit application that generates engaging YouTube video scripts based on a topic, desired video length, and creativity level — enriched with real-time DuckDuckGo search results.

---

## Overview

This tool takes a video topic as input, searches the web for relevant information using DuckDuckGo, and uses Azure OpenAI to generate a catchy title and a full video script tailored to your desired duration and creativity level.

---

## Features

-  Real-time web search via DuckDuckGo to enrich script content
-  AI-generated video title and full script using Azure OpenAI
-  Adjustable creativity slider (0 = focused, 1 = creative)
-  Script length tailored to your target video duration
-  Secure API key input via sidebar

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Azure OpenAI (Chat model) |
| Web Search | DuckDuckGo Search (`duckduckgo-search`) |
| Orchestration | LangChain |

---

## Project Structure
```
├── app.py              # Main Streamlit UI and app logic
├── utils.py            # Script generation logic (LLM + search)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.9+
- An [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) account with a chat model deployment (e.g., `gpt-4o` or `gpt-35-turbo`)

---

## Installation

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd <repo-folder>
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure secrets**

Create a `.streamlit/secrets.toml` file in the project root:
```toml
AZURE_OPENAI_ENDPOINT   = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "your-chat-deployment-name"
```

---

## Usage

**1. Run the app**
```bash
streamlit run app.py
```

**2. In the browser UI:**
- Enter your **Azure OpenAI API key** in the sidebar
- Type in your **video topic**
- Set the **expected video length** (in minutes)
- Adjust the **creativity slider** (0 = precise, 1 = highly creative)
- Click **"Generate Script for me"**

**3. Results:** The app displays:
-  A generated video **title**
-  A full **video script**
-  The **DuckDuckGo search results** used to enrich the script

---

## How It Works
```
User Input (Topic + Duration + Creativity)
            ↓
  DuckDuckGo Search (top 5 results)
            ↓
  Azure OpenAI → Generate Title
            ↓
  Azure OpenAI → Generate Script
  (using Title + Search Data + Duration)
            ↓
    Display in Streamlit UI
```

1. The app searches DuckDuckGo for the given topic and collects the top 5 results.
2. Azure OpenAI generates a compelling video title based on the topic.
3. A full script is generated using the title, search data, and target duration.
4. Results are displayed in the Streamlit UI with an expandable search results section.

---
End of Documentation
---
