# 🚀 AI Analyst Prototype for Startup Evaluation

This is a **Streamlit-based prototype** that evaluates startups by extracting insights from pitch decks (PDF/PPTX) and generating actionable deal notes.

---

## Features

- Upload pitch decks in **PDF** or **PPTX** format
- Extract text content from slides/pages
- Generate **structured deal notes**
- Benchmark startups against peers
- Flag potential risks (e.g., inconsistent metrics)
- Summarize growth potential and provide recommendations

---

## 🔧 Tech Stack

- Python 3
- [Streamlit](https://streamlit.io/) for web interface
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF parsing
- [python-pptx](https://python-pptx.readthedocs.io/) for PPTX parsing
- [Sentence Transformers](https://www.sbert.net/) for embeddings
- Optional: Ngrok for public URL hosting

---

## 📥 Getting Started

## Run in Google Colab

1. Open a new Colab notebook and clone the repo:

```python
!git clone https://github.com/siddth09/ai-analyst-prototype.git
%cd ai-analyst-prototype
```

2. Install dependencies:

```python
!pip install streamlit pypdf2 python-pptx sentence-transformers pyngrok
```

3. Run the app with Ngrok to get a public URL:

```python
from pyngrok import ngrok
import os

# Run Streamlit in the background
!streamlit run app.py &

# Open Ngrok tunnel
public_url = ngrok.connect(8501)
print("Your public Streamlit URL:", public_url)
```

> You can now open the printed `public_url` in any browser to test your app.

---

## 📝 Sample File

* `sample_pitch.pdf` is included for testing the upload functionality.

---

## 💡 Notes

* For **Ngrok**, sign up for a free account to avoid session limits.
* You can add a **password field in Streamlit** for restricted access if sharing with external users.

---

## 📂 Repository Structure

```
ai-analyst-prototype/
├── app.py
├── analyst.py
├── requirements.txt
├── sample_pitch.pdf
├── sample_data/
│   ├── README.md
│   ├── ...
└── README.md
