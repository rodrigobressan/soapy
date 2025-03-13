# SOAPy: AI-Powered Medical Summarizer

SOAPy automates the process of turning unstructured medical notes into organized **SOAP** notes. It uses LLMs to transcribe audio and summarize information, saving time and improving accuracy.

## 💡 How SOAPy Works

1. **Speech-to-Text (Deepgram)**: Dictate your notes, and SOAPy transcribes them into text.
2. **AI Summarization (GPT-4)**: SOAPy organizes the transcribed text into the structured SOAP format:
   - **S**ubjective: Patient’s symptoms and concerns.
   - **O**bjective: Clinician’s findings.
   - **A**ssessment: Diagnosis.
   - **P**lan: Treatment steps.

## 🌐 Live Demo

A Live Demo for it can be found [here](https://soapy-demo.streamlit.app/)


## 🚀 Who Benefits?

- **🏥 Doctors & Nurses**: Streamlines documentation, saving time.
- **📚 Medical Students**: Learn how to write SOAP notes.
- **🚀 HealthTech Innovators**: AI-driven documentation for modern healthcare.

## 🌐 Getting Started

1. **Clone the repo**:
    ```bash
    git clone https://github.com/yourusername/soapy.git
    cd soapy
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set API Keys** (Deepgram & OpenAI GPT-4 related).

4. **Run the app**:
    ```bash
    streamlit run main.py
    ```

## 📑 Example

**Original Doctor's Note**:
- Patient is a 45-year-old male with persistent headaches for two weeks. Blood pressure 140/90 mmHg. No neurological abnormalities. Diagnosed with stress-related tension headaches. Prescribed ibuprofen.

**SOAP Summary**:
- **Subjective**: 45-year-old male with two weeks of headaches. Increased work stress. No nausea.
- **Objective**: BP 140/90 mmHg. Neurological exam normal.
- **Assessment**: Likely tension headaches due to stress.
- **Plan**: Advise stress management. Prescribe ibuprofen. Follow-up in 2 weeks.

## 📦 Technologies

- **Python**
- **Streamlit**
- **Deepgram API (Speech-to-Text)**
- **OpenAI GPT-4 (AI Summarization)**

## ⚡ Contributing

Fork the repo, make changes, and submit a pull request.

## 🔒 License

MIT License. See [LICENSE](LICENSE).
