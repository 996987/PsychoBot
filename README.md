
# PsychoBot - AI Therapist Chatbot

PsychoBot is a supportive chatbot designed to help you with your thoughts and emotions. It uses OpenAI's language models for generating responses and can convert those responses into speech using Google Text-to-Speech (gTTS). The app is built with Streamlit, providing an interactive interface for chatting.

## Features:
- **Conversation Styles**: Choose between different conversation styles: Neutral, Formal, Informal, and Empathetic.
- **Audio Playback**: Option to listen to the chatbot's responses with text-to-speech.
- **Chat History Export**: Export your chat history as a text or PDF file.
- **Local AI Model**: Interact with a locally running OpenAI model for AI-driven responses.

## Prerequisites:
Before running PsychoBot, make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## Installation:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/psychobot.git
   cd psychobot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install OpenAI model (if applicable)**:
   Ensure you have the required OpenAI model running locally or modify the `openai.api_base` in the code to connect to the appropriate endpoint.

5. **Install gTTS for Text-to-Speech**:
   `gTTS` (Google Text-to-Speech) is used for audio generation.
   ```bash
   pip install gtts
   ```

## Usage:

1. **Run the Streamlit app**:
   After installing the dependencies, run the following command to launch the chatbot:

   ```bash
   Home.py
   ```

2. **Interacting with the Chatbot**:
   - Enter your message in the input box and hit "Enter" to start the conversation.
   - The chatbot will respond with a text message and optionally play an audio version of the response if the "Enable Audio Playback" checkbox is checked.
   - You can adjust the conversation style and playback options using the sidebar.
   - You can also start a new chat, and export your chat history as either a `.txt` or `.pdf` file.

3. **Exporting Chat History**:
   - Use the "Export as TXT" or "Export as PDF" buttons on the sidebar to download the current chat history.

## Code Overview:

- **`app.py`**: The main Streamlit app where the chatbot interface and logic reside.
- **`chat_with_psychobot()`**: Function for sending user input to the local OpenAI model and getting a response.
- **`play_audio()`**: Function for generating and playing the bot's response as audio using `gTTS` (Google Text-to-Speech).
- **`export_chat_history()`**: Function to export chat history as a `.txt` or `.pdf` file.

## Configuration:

- **Conversation Style**: You can choose between different tones:
  - **Neutral**: Empathetic, like a psychologist.
  - **Formal**: Professional and polite.
  - **Informal**: Friendly and relaxed.
  - **Empathetic**: Shows empathy and understanding.
  
- **Temperature**: Controls the creativity of the AI's responses (higher values make the responses more creative).

- **Max Tokens**: Controls the maximum length of the AI's response.

## Troubleshooting:

- **Audio not playing**: Ensure that your browser allows autoplay for audio. If you're using Streamlit locally, make sure the correct port (default 8501) is open in your browser.
- **Error with OpenAI API**: If you're using a local OpenAI model, ensure it is properly running and accessible via the specified `openai.api_base`.

## License:

This project is open-source and available under the [MIT License](LICENSE).
