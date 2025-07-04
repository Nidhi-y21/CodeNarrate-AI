# CodeNarrate-AI

**CodeNarrate AI** is a real-time code narrator that explains and optionally speaks Python code as it executes. 
Built using Azure OpenAI and Azure Cognitive Services, it helps learners and developers understand code logic step-by-step.

## 🔧 Features
- Traces Python scripts line by line
- Uses Azure OpenAI (GPT-4) to generate natural language explanations
- Optionally narrates explanations aloud using Azure Text-to-Speech
- CLI-based, lightweight, and customizable

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/codenarrate-ai.git
cd codenarrate-ai
```

### 2. Setup Environment
- Rename `.env.example` to `.env`
- Fill in your Azure API keys:
```bash
AZURE_OPENAI_KEY=your_openai_key
AZURE_SPEECH_KEY=your_speech_key
AZURE_SPEECH_REGION=your_region
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the Project
```bash
python app/runner.py test_scripts/sample.py
```

## 🧠 Tech Stack
- Python
- Azure OpenAI Service
- Azure Cognitive Services (Speech SDK)

## 📂 Project Structure
```
app/
  ├── tracer.py     # Code execution tracer
  ├── narrator.py   # GPT-based explainer
  ├── speaker.py    # Azure TTS narrator
  └── runner.py     # Main CLI entry point
test_scripts/
  └── sample.py     # Sample script to test
.env.example         # Template for Azure keys
```

## 📸 Sample Output
```
Line 2: name = "World"
Explanation: This line stores the word 'World' into the variable 'name'.

Line 3: print("Hello, " + name)
Explanation: This line prints the greeting by combining 'Hello, ' and the name.
```

## ✨ Future Scope
- Turn into a VS Code extension
- Add support for other languages
- Streamlit/Flask Web UI
- Multilingual narration

## 📜 License
MIT License

## 🤝 Acknowledgements
Built during the AICTE–Microsoft Virtual Internship 2025, mentored by Edunet Foundation.
