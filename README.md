# PDF Summarizer AI

AI-powered PDF summarizer built using Python, Flask, NLP, and Semantic Embeddings.

## Features

* Upload PDF files
* Max 5 pages
* Smart 50–60% summarization
* Semantic ranking
* MMR repetition removal
* Topic clustering
* Structured bullet-point output
* Modern dark UI

---

# Technologies

* Python
* Flask
* Sentence Transformers
* FLAN-T5
* HTML/CSS

---

# Installation

## Create Virtual Environment

```bash id="jlwmn7"
python -m venv venv
```

---

## Activate Environment

### Windows

```bash id="jlwmn8"
venv\Scripts\activate
```

---

## Install Requirements

```bash id="jlwmn9"
pip install -r requirements.txt
```

---

# Run Project

```bash id="jlwmna"
python app.py
```

---

# Open In Browser

```text id="jlwmm1"
http://127.0.0.1:5000
```

---

# Recommended Python Version

```text id="jlwmnb"
Python 3.10
```

---

# Project Structure

```text id="jlwmnc"
pdf_summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── uploads/
```
