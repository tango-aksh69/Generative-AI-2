# ✨ AI Story & Poem Generator

An interactive web application built with Streamlit and OpenAI's API that acts as your personal AI muse. It allows you to generate custom, creative stories and poems simply by providing a prompt, genre, and length.

## Features
- **Story Generation**: Choose a genre (Fantasy, Mystery, Romance, Horror, Adventure), select a length (Short, Medium, Long), and provide an idea.
- **Poem Generation**: Pick your preferred poem style (Rhyming, Haiku, Free Verse, Limerick) and enter your topic.
- **Downloadable Output**: Easily download the generated story or poem as a pure text file directly from the app interface.
- **Clean and Simple UI**: Intuitive one-page design with no complicated navigation, keeping everything on the main screen.

## Prerequisites
- Python 3.8+
- An active OpenAI API Key

## Installation

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/tango-aksh69/Gen-AI-Project.git>
   cd "Gen-AI Project"
   ```

2. **Install dependencies:**
   Make sure you have `streamlit` and `openai` installed.
   ```bash
   pip install streamlit openai
   ```

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```
2. **Access the Web Interface:** It should automatically open in your default browser at `http://localhost:8501`.
3. **Generate Content:**
   - Securely enter your OpenAI API key.
   - Choose whether to generate a Story or a Poem from the dropdowns.
   - Provide your prompt (e.g. "A dragon who is afraid of fire") and hit "Generate".
   - Download the result using the "Download as Text File" button at the bottom once generation is complete.

## Built With
- [Streamlit](https://streamlit.io/) - App UI framework
- [OpenAI](https://openai.com/) - Engine behind the AI generation (GPT-3.5-turbo)

## License
Available as open source.
