# PDF Summarizer AI

AI-powered PDF summarizer built using Python, Flask, NLP, Semantic Embeddings, and Transformer Models.

## Features

* Upload PDF files
* Maximum 5 pages
* Text-based PDFs only
* Intelligent 50–60% summarization
* Semantic sentence ranking
* MMR diversity selection
* Topic clustering
* Structured bullet-point output
* Modern dark UI
* PDF export support

---

# Technologies Used

## Backend

* Python
* Flask

## AI & NLP

* Sentence Transformers
* FLAN-T5
* KMeans Clustering
* Semantic Embeddings

## Frontend

* HTML
* CSS
* JavaScript

---

# AI Pipeline

1. Extract PDF text
2. Clean and split sentences
3. Rank important sentences
4. Remove repetition using MMR
5. Cluster topics
6. Generate structured summary

---

# Installation

## Clone Repository

```bash id="jlwmn3"
git clone YOUR_REPOSITORY_LINK
```

---

## Open Project Folder

```bash id="1hyj5j"
cd pdf_summarizer
```

---

## Create Virtual Environment

```bash id="r7o85m"
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash id="v4yxqs"
venv\Scripts\activate
```

---

## Install Dependencies

```bash id="l2dx6f"
pip install -r requirements.txt
```

---

# Run Project

```bash id="9slxtt"
python app.py
```

---

# Open In Browser

```text id="t4b0ul"
http://127.0.0.1:5000
```

---

# Recommended Python Version

```text id="jlwmn4"
Python 3.10
```

---

# Project Structure

```text id="jlwmn5"
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
│   ├── style.css
│
└── uploads/
```

---

# Frontend Files

## index.html

Located inside:

```text id="7v8x7n"
templates/index.html
```

Used for:

* Main UI
* PDF upload form
* Summary display

---

## style.css

Located inside:

```text id="8r9w7n"
static/style.css
```

Used for:

* Dark modern UI
* Layout styling
* Responsive design
* Animations

---

## script.js

Located inside:

```text id="v2c7nb"
static/script.js
```

Used for:

* Loading animation
* Frontend interactions
* UI enhancements
