import re
import fitz
import numpy as np

from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline


# =========================================
# MODELS
# =========================================

embed_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

heading_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


# =========================================
# PDF EXTRACTION
# =========================================

def extract_text(pdf_file):

    doc = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    if len(doc) > 5:
        return "Error: Maximum 5 pages allowed."

    text = ""

    for page in doc:
        text += page.get_text()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =========================================
# CLEAN SENTENCES
# =========================================

def clean_sentences(sentences):

    cleaned = []

    for s in sentences:

        s = s.strip()

        if len(s) < 30:
            continue

        if len(s.split()) < 6:
            continue

        if s.lower() in [x.lower() for x in cleaned]:
            continue

        cleaned.append(s)

    return cleaned


# =========================================
# FACT BOOSTING
# =========================================

def contains_fact(sentence):

    patterns = [
        r"\d+",
        r"\%",
        r"\$",
        r"million",
        r"billion",
        r"research",
        r"study",
        r"data",
        r"statistics",
        r"analysis",
        r"year"
    ]

    for p in patterns:
        if re.search(p, sentence.lower()):
            return True

    return False


# =========================================
# TITLE EXTRACTION
# =========================================

def extract_title(sentences):

    if len(sentences) == 0:
        return ""

    return sentences[0]


# =========================================
# HYBRID SCORING
# =========================================

def calculate_scores(sentences):

    embeddings = embed_model.encode(sentences)

    centroid = np.mean(
        embeddings,
        axis=0
    )

    title = extract_title(sentences)

    title_embedding = embed_model.encode([title])[0]

    scores = []

    total_sentences = len(sentences)

    for i, emb in enumerate(embeddings):

        score = 0

        # Semantic centrality
        semantic_score = cosine_similarity(
            [emb],
            [centroid]
        )[0][0]

        score += semantic_score * 0.45

        # Title relevance
        title_score = cosine_similarity(
            [emb],
            [title_embedding]
        )[0][0]

        score += title_score * 0.25

        # Positional importance
        if i < total_sentences * 0.15:
            score += 0.15

        elif i > total_sentences * 0.85:
            score += 0.10

        # Fact boosting
        if contains_fact(sentences[i]):
            score += 0.20

        # Longer informative sentences
        if len(sentences[i].split()) > 14:
            score += 0.05

        scores.append(score)

    return embeddings, scores


# =========================================
# MMR SELECTION
# =========================================

def mmr_selection(
    sentences,
    embeddings,
    scores,
    retention_ratio=0.55,
    lambda_param=0.70
):

    total_words = sum(
        len(s.split())
        for s in sentences
    )

    target_words = int(
        total_words * retention_ratio
    )

    selected = []

    selected_indexes = []

    current_words = 0

    ranked_indexes = np.argsort(scores)[::-1]

    # First best sentence
    first = ranked_indexes[0]

    selected.append(sentences[first])

    selected_indexes.append(first)

    current_words += len(
        sentences[first].split()
    )

    # MMR loop
    while current_words < target_words:

        best_idx = None
        best_score = -999

        for idx in ranked_indexes:

            if idx in selected_indexes:
                continue

            relevance = scores[idx]

            diversity = max([
                cosine_similarity(
                    [embeddings[idx]],
                    [embeddings[j]]
                )[0][0]
                for j in selected_indexes
            ])

            mmr = (
                lambda_param * relevance
                -
                (1 - lambda_param) * diversity
            )

            if mmr > best_score:
                best_score = mmr
                best_idx = idx

        if best_idx is None:
            break

        selected.append(
            sentences[best_idx]
        )

        selected_indexes.append(
            best_idx
        )

        current_words += len(
            sentences[best_idx].split()
        )

    # Preserve original order
    ordered = sorted(selected_indexes)

    return [
        sentences[i]
        for i in ordered
    ]


# =========================================
# REMOVE REPETITION
# =========================================

def remove_redundancy(
    sentences,
    threshold=0.82
):

    if len(sentences) <= 1:
        return sentences

    embeddings = embed_model.encode(sentences)

    filtered = []

    kept_indexes = []

    for i, sentence in enumerate(sentences):

        duplicate = False

        for kept_idx in kept_indexes:

            similarity = cosine_similarity(
                [embeddings[i]],
                [embeddings[kept_idx]]
            )[0][0]

            if similarity > threshold:
                duplicate = True
                break

        if not duplicate:
            filtered.append(sentence)
            kept_indexes.append(i)

    return filtered


# =========================================
# CLUSTERING
# =========================================

def cluster_sentences(sentences):

    if len(sentences) <= 2:
        return {0: sentences}

    embeddings = embed_model.encode(sentences)

    cluster_count = min(
        5,
        max(2, len(sentences) // 5)
    )

    if cluster_count > len(sentences):
        cluster_count = len(sentences)

    kmeans = KMeans(
        n_clusters=cluster_count,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(
        embeddings
    )

    grouped = {}

    for i, label in enumerate(labels):

        grouped.setdefault(
            label,
            []
        ).append(sentences[i])

    return grouped


# =========================================
# HEADING GENERATION
# =========================================

def generate_heading(sentences):

    text = " ".join(sentences[:3])

    prompt = f"""
Generate a short professional heading:

{text}
"""

    result = heading_model(
        prompt,
        max_new_tokens=8,
        do_sample=False
    )

    heading = result[0][
        "generated_text"
    ].strip()

    heading = heading.title()

    if len(heading) < 4:
        heading = "Key Insights"

    return heading


# =========================================
# STRUCTURED OUTPUT
# =========================================

def build_output(clusters):

    structured = {}

    for _, sentence_group in clusters.items():

        heading = generate_heading(
            sentence_group
        )

        clean_group = []

        for s in sentence_group:

            s = s.strip()

            if not s.endswith("."):
                s += "."

            s = s[0].upper() + s[1:]

            if s not in clean_group:
                clean_group.append(s)

        structured[heading] = clean_group

    return structured


# =========================================
# MAIN PIPELINE
# =========================================

def summarize_pdf(pdf_file):

    text = extract_text(pdf_file)

    if text.startswith("Error"):
        return text

    sentences = sent_tokenize(text)

    sentences = clean_sentences(
        sentences
    )

    if len(sentences) == 0:
        return {
            "Error": [
                "No meaningful text found."
            ]
        }

    embeddings, scores = calculate_scores(
        sentences
    )

    important = mmr_selection(
        sentences,
        embeddings,
        scores,
        retention_ratio=0.55
    )

    important = remove_redundancy(
        important
    )

    clusters = cluster_sentences(
        important
    )

    final_output = build_output(
        clusters
    )

    return final_output