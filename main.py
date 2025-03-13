import streamlit as st
import openai
import requests
import os
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

# Load API keys from .env file
load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)


# Function to transcribe audio using Deepgram
def transcribe_audio(audio_bytes):
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "audio/wav"
    }
    response = requests.post("https://api.deepgram.com/v1/listen", headers=headers, data=audio_bytes)
    return response.json().get("results", {}).get("channels", [{}])[0].get("alternatives", [{}])[0].get("transcript",
                                                                                                        "")


# Function to summarize text using OpenAI GPT-4
def summarize_medical_notes(text):
    prompt = f"""You are a medical assistant. Convert the following doctor’s note into a structured SOAP format (Subjective, Objective, Assessment, Plan):\n\n{text}\n"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a medical assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# Streamlit UI Configuration
st.set_page_config(page_title="Medical Note Summarizer", layout="wide", initial_sidebar_state="expanded")

# Sidebar Navigation with Stylish Option Menu
with st.sidebar:
    page = option_menu(
        menu_title="🧼 SOAPy",
        options=["How It Works", "Example", "Upload & Summarize", ],
        icons=["info-circle", "book", "file-text"],
        menu_icon="none",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "color": "#333"},
            "nav-link-selected": {"background-color": "#2E7D32", "color": "white"},
        },
    )

# Upload & Summarize Page
if page == "Upload & Summarize":
    st.title("📤 Upload & Summarize Medical Notes")
    st.markdown(
        "Upload an audio file of a doctor's note, and SOAPy will transcribe and summarize it into SOAP format.")

    uploaded_file = st.file_uploader(
        "Upload your doctor's note (WAV, MP3, M4A)",
        type=["wav", "mp3", "m4a"],
        help="Only audio files are supported."
    )

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")

        if st.button("Summarize Medical Note 📝", use_container_width=True):
            with st.spinner("Processing..."):
                audio_bytes = uploaded_file.getvalue()
                transcript = transcribe_audio(audio_bytes)
                summary = summarize_medical_notes(transcript)

                st.success("✅ Summarization complete!")
                st.subheader("📜 Transcript:")
                st.text_area("", transcript, height=150)
                st.subheader("📝 SOAP Summary:")
                st.text_area("", summary, height=200)

# Example Page
elif page == "Example":
    st.title("📑 Example: Medical Note to SOAP Summary")

    st.markdown("""
        ### Sample Doctor’s Note:
        Below is an example of a **typical medical note** written by a physician.  
        The AI will then **convert it into the SOAP format** for better readability and structure.
    """)

    sample_note = """
    Patient is a 45-year-old male complaining of persistent headaches for the past two weeks. 
    Reports no history of migraines but mentions recent increased work stress. 
    No nausea or vomiting. Blood pressure today is 140/90 mmHg. 
    Neurological exam is unremarkable. No signs of infection or trauma. 
    Suspected stress-related tension headaches. Recommended stress management techniques 
    and prescribed ibuprofen 400mg as needed. Follow-up in two weeks if symptoms persist.
    """

    st.text_area("📋 Original Doctor’s Note:", sample_note, height=150)

    sample_soap = """
    **Subjective:** 45-year-old male with persistent headaches for two weeks. No history of migraines. Reports increased work stress. No associated nausea or vomiting.  

    **Objective:** Blood pressure: 140/90 mmHg. Neurological exam unremarkable. No signs of infection or trauma.  

    **Assessment:** Likely tension headaches due to stress.  

    **Plan:** Advise stress management techniques. Prescribe ibuprofen 400mg PRN. Follow-up in two weeks if symptoms persist.
    """

    st.text_area("📝 SOAP Summary:", sample_soap, height=200)

    st.markdown("""
        **🔍 Why is SOAPy useful?**
        - Makes **medical notes clearer & structured** for doctors and nurses.  
        - Helps in **electronic health record (EHR) documentation**.  
        - Assists **students** in learning how to write SOAP notes effectively.  
    """)

# How It Works Page
elif page == "How It Works":
    st.title("💡 How It Works")
    st.markdown("""
        SOAPy helps **healthcare professionals, medical students, and healthtech innovators** by converting unstructured medical notes into a structured **SOAP format** using AI.

        **Navigate to the 'Upload & Summarize' page to start using it, or check the 'Example' page to see how it works!**

        SOAPy **automates medical documentation** by combining **speech-to-text** and **natural language processing**.

        - **🎙️ Speech-to-Text (Deepgram):** Converts audio notes into text.
        - **🧠 AI Summarization (GPT-4):** Extracts key medical details and structures them into **SOAP format**.

        **Who benefits from this?**
        - 🏥 **Doctors & Nurses**: Faster and more organized documentation.  
        - 📚 **Medical Students**: Learn how to write structured SOAP notes.  
        - 🚀 **HealthTech Innovators**: AI-powered documentation for modern healthcare.
    """)

# About Page
elif page == "About":
    st.title("📌 About This Project")
    st.markdown("""
        SOAPy eases medical documentation using AI-powered **speech recognition** and **text summarization**.

        - 🎙️ **Deepgram** (Speech-to-Text)  
        - 🧠 **OpenAI GPT-4** (Summarization)  
        - 🎨 **Streamlit** (UI Framework)

        **Join us in making medical documentation faster and more efficient! 🚀**
    """)
