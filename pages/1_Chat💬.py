import streamlit as st
import openai
from fpdf import FPDF
import os
from tempfile import NamedTemporaryFile
import logging
from gtts import gTTS

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Streamlit Page Config
st.set_page_config(page_title="PsychoBot - AI Therapist", page_icon="💬", layout="centered")

# Function to export chat history
def export_chat_history(format="txt"):
    try:
        chat_history = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state["messages"]]
        )
        if format == "txt":
            with NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
                temp_file.write(chat_history.encode("utf-8"))
                st.download_button(
                    label="💾 Download Chat as TXT",
                    data=chat_history,
                    file_name="chat_history.txt",
                    mime="text/plain"
                )
        elif format == "pdf":
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in chat_history.split("\n"):
                pdf.cell(200, 10, txt=line, ln=True)
            with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                pdf.output(temp_file.name)
                st.download_button(
                    label="📄 Download Chat as PDF",
                    data=open(temp_file.name, "rb").read(),
                    file_name="chat_history.pdf",
                    mime="application/pdf"
                )
    except Exception as e:
        st.error(f"⚠️ Error exporting chat history: {e}")
        logging.error(f"Error exporting chat history: {e}")

# Sidebar Styling
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    st.divider()

    enable_audio = st.checkbox("🔊 Enable Audio Playback", value=True)
    st.divider()
    
    # Conversation Style
    style = st.selectbox("🗣️ Style", options=["Neutral", "Formal", "Informal", "Empathetic"])
    st.divider()

    # Temperature Slider
    temperature = st.slider("🌡️ Temperature", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
    st.divider()

    # Max Tokens Slider
    max_tokens = st.slider("🔢 Max Tokens", min_value=20, max_value=300, value=80, step=10)
    st.divider()

    # Start New Chat Button
    if st.button("🔄 Start New Chat"):
        st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you today?"}]
        st.session_state["is_new_chat"] = True

    # Export Chat History
    st.markdown("### 💾 Export Chat History")
    if st.button("Export as TXT"):
        export_chat_history(format="txt")
    if st.button("Export as PDF"):
        export_chat_history(format="pdf")

# OpenAI API Setup
openai.api_base = "http://127.0.0.1:1234/v1"
openai.api_key = "not-needed"

# Function to interact with the local AI model
def chat_with_psychobot(user_input, style, temperature, max_tokens):
    tones = {
        "Formal": "Be very formal, polite, and professional.",
        "Informal": "Respond in a friendly and relaxed manner.",
        "Empathetic": "Show empathy and understanding.",
        "Neutral": "Act like you are my psychologist and be empathetic."
    }

    try:
        response = openai.ChatCompletion.create(
            model="local-model",
            messages=[
                {"role": "system", "content": f"{tones.get(style, ' ')}"},
                {"role": "user", "content": user_input}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return f"⚠️ Error generating response: {e}"
    


def play_audio(bot_response):
    try:
        # Create a temporary directory for audio files
        temp_dir = "custom_temp"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Generate speech from text
        with NamedTemporaryFile(delete=False, dir=temp_dir, suffix=".mp3") as temp_audio:
            tts = gTTS(bot_response, lang="en")
            tts.save(temp_audio.name)
            audio_path = temp_audio.name  # Save file path

        # Display hidden audio player
        st.audio(audio_path, format="audio/mp3")

        # Inject JavaScript for autoplay
        st.markdown(
            f"""
            <script>
            var audio = new Audio('{audio_path}');
            audio.play();
            </script>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        logging.error(f"Audio playback error: {e}")
        st.error(f"⚠️ Audio playback error: {e}")
    finally:
        # Ensure the temporary file is deleted
        if os.path.exists(temp_audio.name):
            os.remove(temp_audio.name)


# Chat Interface
def chat_interface():
    st.title("💬 PsychoBot - Your AI Therapist")
    st.caption("A supportive chatbot designed to help you with your thoughts and emotions.")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
        st.session_state["is_new_chat"] = True

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input field
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # Show bot response with a loading spinner
        with st.spinner("Thinking..."):
            bot_response = chat_with_psychobot(user_input, style, temperature, max_tokens)

        # Display bot's response
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.chat_message("assistant").write(bot_response)

            # Play response audio if enabled
        if enable_audio:
            play_audio(bot_response)

# Run the chatbot
if __name__ == "__main__":
    chat_interface()
