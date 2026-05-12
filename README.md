# PDF Summarizer AI

An advanced AI-powered PDF summarization web application built using Python, Flask, NLP, Semantic Embeddings, and Transformer Models.

This project extracts text from PDF files and generates a structured hierarchical summary with:

* Smart semantic ranking
* Topic clustering
* MMR diversity selection
* AI-generated headings
* Fact preservation
* 50–60% intelligent retention

---

# Features

## AI Pipeline

### Stage 1 — Semantic Extraction

* Extracts text from PDF
* Splits into sentences
* Cleans noisy/repetitive content

### Stage 2 — Intelligent Ranking

Uses hybrid scoring:

* Semantic centrality
* Title-aware relevance
* Positional importance
* Fact boosting
* Informative sentence weighting

### Stage 3 — MMR Diversity Selection

Uses Maximal Marginal Relevance (MMR):

* Reduces repetition
* Preserves topic diversity
* Keeps important information

### Stage 4 — Topic Clustering

Groups related content using:

* Sentence embeddings
* KMeans clustering

### Stage 5 — Structured Output

Generates:

* Smart topic headings
* Structured bullet points
* Logical grouping

---

# Key Technologies

## Backend

* Python
* Flask

## NLP & AI

* Sentence Transformers
* FLAN-T5
* Semantic Embeddings
* MMR Algorithm
* KMeans Clustering

## Frontend

* HTML
* CSS
* JavaScript

---

# AI Models Used

## Embedding Model

```python
all-MiniLM-L6-v2
```

Used for:

* Semantic similarity
* Ranking
* Clustering
* Redundancy detection

---

## Transformer Model

```python
google/flan-t5-base
```

Used for:

* Heading generation
* Structured formatting

---

# Advanced Features

* Semantic extractive summarization
* Hybrid ranking system
* Title-aware scoring
* Positional importance scoring
* Fact preservation
* Diversity-aware selection
* Topic clustering
* Smart heading generation
* Modern dark UI
* PDF export support

---

# Input Constraints

* Maximum 5 pages
* Text-based PDFs only
* English language support

---

# Retention Logic

Unlike traditional summarizers that heavily compress information, this project preserves approximately:

```text
50–60% of important content
```

This improves:

* Detail preservation
* Factual accuracy
* Topic coverage
* Readability

---

# Project Structure

```text
pdf_summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/
```

---

# Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2. Open Project Folder

```bash
cd pdf_summarizer
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python app.py
```

---

# Open In Browser

```text
http://127.0.0.1:5000
```

---

# Example Workflow

1. Upload PDF
2. Extract text
3. Semantic ranking
4. MMR selection
5. Topic clustering
6. Structured summary generation
7. Export summary

---

# Algorithms Used

## Semantic Similarity

Measures sentence importance using embeddings.

---

## MMR (Maximal Marginal Relevance)

Balances:

* relevance
* diversity

Prevents repetitive summaries.

---

## KMeans Clustering

Groups semantically related sentences into topics.

---

# Future Improvements

* Multi-language support
* OCR for image PDFs
* Better heading generation
* KeyBERT keyword extraction
* Advanced PDF export styling
* Async processing
* GPU optimization

---

# Python Version

Recommended:

```text
Python 3.10
```

---

# License

MIT License

---

# Author

Developed as an AI + NLP backend-heavy project using:

* Semantic AI
* Transformer Models
* NLP Pipelines
* Modern Web Technologies
