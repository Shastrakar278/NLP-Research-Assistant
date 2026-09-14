import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# TF-IDF SIMILARITY
# ============================================================

def tfidf_similarity(text1, text2):

    if not text1 or not text2:
        return 0.0

    try:

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        matrix = vectorizer.fit_transform(
            [text1, text2]
        )

        score = cosine_similarity(
            matrix[0:1],
            matrix[1:2]
        )[0][0]

        return score * 100

    except Exception:
        return 0.0


# ============================================================
# WORD OVERLAP
# ============================================================

def word_overlap(text1, text2):

    if not text1 or not text2:
        return 0.0

    words1 = set(
        re.findall(
            r"\b[a-zA-Z]{3,}\b",
            text1.lower()
        )
    )

    words2 = set(
        re.findall(
            r"\b[a-zA-Z]{3,}\b",
            text2.lower()
        )
    )

    if not words1 or not words2:
        return 0.0

    intersection = words1 & words2
    union = words1 | words2

    return (
        len(intersection)
        / len(union)
    ) * 100


# ============================================================
# N-GRAM SIMILARITY
# ============================================================

def ngram_similarity(text1, text2):

    if not text1 or not text2:
        return 0.0

    try:

        vectorizer = TfidfVectorizer(
            ngram_range=(3, 3),
            stop_words="english"
        )

        matrix = vectorizer.fit_transform(
            [text1, text2]
        )

        score = cosine_similarity(
            matrix[0:1],
            matrix[1:2]
        )[0][0]

        return score * 100

    except Exception:
        return 0.0


# ============================================================
# ADVANCED SIMILARITY SCORE
# ============================================================

def advanced_similarity(text1, text2):

    tfidf = tfidf_similarity(
        text1,
        text2
    )

    ngram = ngram_similarity(
        text1,
        text2
    )

    overlap = word_overlap(
        text1,
        text2
    )

    # Weighted combined score
    score = (
        tfidf * 0.50
        + ngram * 0.30
        + overlap * 0.20
    )

    return round(
        score,
        2
    )


# ============================================================
# CALCULATE SIMILARITY WITH MULTIPLE SOURCES
# ============================================================

def calculate_similarity(
    generated_text,
    source_texts
):

    scores = []

    if not generated_text:
        return scores

    if not source_texts:
        return scores

    for source in source_texts:

        if source:

            score = advanced_similarity(
                generated_text,
                source
            )

            scores.append(
                score
            )

    return scores


# ============================================================
# GET AVERAGE SIMILARITY
# ============================================================

def average_similarity(scores):

    if not scores:
        return 0.0

    return round(
        sum(scores) / len(scores),
        2
    )


# ============================================================
# GET HIGHEST SIMILARITY
# ============================================================

def highest_similarity(scores):

    if not scores:
        return 0.0

    return round(
        max(scores),
        2
    )


# ============================================================
# SIMILARITY REPORT
# ============================================================

def generate_similarity_report(
    generated_text,
    source_texts
):

    scores = calculate_similarity(
        generated_text,
        source_texts
    )

    average_score = average_similarity(
        scores
    )

    highest_score = highest_similarity(
        scores
    )

    return {
        "scores": scores,
        "average_similarity": average_score,
        "highest_similarity": highest_score,
        "number_of_sources": len(scores)
    }
