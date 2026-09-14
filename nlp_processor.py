import re
from collections import Counter


# ============================================================
# STOPWORDS
# ============================================================

STOPWORDS = {
    "the", "and", "for", "with", "that", "this",
    "from", "are", "was", "were", "have", "has",
    "using", "used", "into", "based", "their",
    "which", "these", "than", "also", "such",
    "between", "through", "been", "can", "may",
    "our", "they", "its", "not", "but", "this",
    "those", "then", "than", "there", "where",
    "when", "while", "study", "research", "paper"
}


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_text(text):

    if not text:
        return ""

    text = text.lower()

    # Remove extra spaces and new lines
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# KEYWORD EXTRACTION
# ============================================================

def extract_keywords(text, top_n=10):

    if not text:
        return []

    words = re.findall(
        r"\b[a-zA-Z]{4,}\b",
        text.lower()
    )

    words = [
        word
        for word in words
        if word not in STOPWORDS
    ]

    counter = Counter(words)

    return [
        word
        for word, _ in counter.most_common(top_n)
    ]


# ============================================================
# SECTION EXTRACTION
# ============================================================

def extract_section(
    text,
    section_names,
    max_chars=1500
):

    if not text:
        return ""

    section_pattern = "|".join(
        re.escape(name)
        for name in section_names
    )

    next_sections = (
        r"abstract|introduction|background|"
        r"literature review|methodology|method|"
        r"methods|materials and methods|"
        r"results|findings|discussion|"
        r"limitations|future work|"
        r"future scope|conclusion|"
        r"references"
    )

    pattern = (
        r"(?i)(?:"
        + section_pattern
        + r")"
        r"\s*:?\s*"
        r"(.*?)"
        r"(?=\n\s*(?:"
        + next_sections
        + r")\b|$)"
    )

    match = re.search(
        pattern,
        text,
        re.DOTALL
    )

    if match:

        result = match.group(1).strip()

        return result[:max_chars]

    return ""


# ============================================================
# EXTRACT INFORMATION FROM ONE PAPER
# ============================================================

def extract_information(text):

    if not text:
        return {
            "keywords": [],
            "introduction": "",
            "methodology": "",
            "results": "",
            "limitations": "",
            "conclusion": ""
        }

    cleaned = clean_text(text)

    return {

        "keywords": extract_keywords(
            cleaned,
            top_n=10
        ),

        "introduction": extract_section(
            text,
            [
                "introduction",
                "background"
            ]
        ),

        "methodology": extract_section(
            text,
            [
                "methodology",
                "method",
                "methods",
                "materials and methods"
            ]
        ),

        "results": extract_section(
            text,
            [
                "results",
                "findings",
                "experimental results"
            ]
        ),

        "limitations": extract_section(
            text,
            [
                "limitations",
                "limitations of the study"
            ]
        ),

        "conclusion": extract_section(
            text,
            [
                "conclusion",
                "conclusions"
            ]
        )
    }


# ============================================================
# ANALYZE MULTIPLE RESEARCH PAPERS
# ============================================================

def analyze_papers(papers):

    analysis = []

    for paper in papers:

        text = paper.get(
            "text",
            ""
        )

        information = extract_information(
            text
        )

        analysis.append({

            "title": paper.get(
                "title",
                "Unknown"
            ),

            "year": paper.get(
                "year",
                "N/A"
            ),

            "authors": paper.get(
                "authors",
                []
            ),

            "keywords": information[
                "keywords"
            ],

            "introduction": information[
                "introduction"
            ],

            "methodology": information[
                "methodology"
            ],

            "results": information[
                "results"
            ],

            "limitations": information[
                "limitations"
            ],

            "conclusion": information[
                "conclusion"
            ]
        })

    return analysis


# ============================================================
# COMMON KEYWORDS FROM MULTIPLE PAPERS
# ============================================================

def find_common_keywords(
    paper_analyses,
    top_n=15
):

    all_keywords = []

    for paper in paper_analyses:

        keywords = paper.get(
            "keywords",
            []
        )

        all_keywords.extend(
            keywords
        )

    counter = Counter(
        all_keywords
    )

    return [
        word
        for word, _ in counter.most_common(
            top_n
        )
    ]


# ============================================================
# CREATE NLP ANALYSIS SUMMARY
# ============================================================

def generate_nlp_summary(
    topic,
    paper_analyses
):

    common_keywords = find_common_keywords(
        paper_analyses
    )

    keyword_text = ", ".join(
        common_keywords
    )

    return {
        "topic": topic,

        "number_of_papers": len(
            paper_analyses
        ),

        "common_keywords": common_keywords,

        "summary": (
            f"NLP analysis for '{topic}' "
            f"was performed on "
            f"{len(paper_analyses)} research papers. "
            f"Important concepts identified from "
            f"the literature include: "
            f"{keyword_text}."
        )
    }
