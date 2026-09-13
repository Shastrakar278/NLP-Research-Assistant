import re
from collections import Counter


# ============================================================
# TEXT HELPERS
# ============================================================

def clean_text(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", str(text)).strip()


def limit_text(text, max_chars=2500):
    text = clean_text(text)
    return text[:max_chars]


def get_title(paper):
    return paper.get("title", "Unknown Research Paper")


def get_year(paper):
    return paper.get("year", "N/A")


def get_authors(paper):
    authors = paper.get("authors", [])
    if isinstance(authors, list):
        return ", ".join(authors[:5])
    return str(authors)


def get_abstract(paper):
    return clean_text(paper.get("abstract", ""))


# ============================================================
# TOPIC ANALYSIS
# ============================================================

def extract_topic_keywords(topic):
    words = re.findall(r"\b[a-zA-Z]{3,}\b", topic.lower())

    stopwords = {
        "the", "and", "for", "with", "using", "based",
        "system", "model", "approach", "study", "development",
        "analysis", "application", "intelligent"
    }

    return [w for w in words if w not in stopwords]


def get_topic_domain(topic):
    t = topic.lower()

    if any(x in t for x in ["mango", "fruit", "ripening", "apple", "banana", "papaya"]):
        return "fruit monitoring and ripening"

    if any(x in t for x in ["e-learning", "elearning", "education", "course recommendation"]):
        return "e-learning and educational recommendation"

    if any(x in t for x in ["text classification", "sentiment", "nlp", "natural language"]):
        return "natural language processing and text analysis"

    if any(x in t for x in ["iot", "internet of things", "sensor"]):
        return "IoT and sensor-based monitoring"

    if any(x in t for x in ["healthcare", "disease", "medical", "health"]):
        return "healthcare and intelligent prediction"

    if any(x in t for x in ["smart home", "home automation"]):
        return "smart home automation"

    if any(x in t for x in ["recommendation", "recommender"]):
        return "recommendation systems"

    if any(x in t for x in ["image", "vision", "classification"]):
        return "computer vision and classification"

    return "artificial intelligence and intelligent systems"


# ============================================================
# PAPER RELEVANCE
# ============================================================

def calculate_topic_relevance(topic, paper):
    topic_words = set(extract_topic_keywords(topic))

    text = " ".join([
        get_title(paper),
        get_abstract(paper)
    ]).lower()

    paper_words = set(re.findall(r"\b[a-zA-Z]{3,}\b", text))

    if not topic_words:
        return 0

    common = topic_words.intersection(paper_words)

    return len(common) / len(topic_words)


def get_relevant_papers(topic, papers, count=5):
    ranked = []

    for paper in papers:
        score = calculate_topic_relevance(topic, paper)
        ranked.append((score, paper))

    ranked.sort(key=lambda x: x[0], reverse=True)

    return [paper for _, paper in ranked[:count]]


# ============================================================
# COMMON KEYWORDS FROM RESEARCH PAPERS
# ============================================================

def extract_common_keywords(topic, papers, top_n=12):

    topic_words = set(extract_topic_keywords(topic))

    all_words = []

    for paper in papers:
        text = " ".join([
            get_title(paper),
            get_abstract(paper)
        ]).lower()

        words = re.findall(r"\b[a-zA-Z]{4,}\b", text)

        for word in words:
            if word not in topic_words:
                all_words.append(word)

    stopwords = {
        "this", "that", "these", "those", "with", "from",
        "using", "used", "based", "their", "which", "were",
        "have", "been", "into", "also", "such", "between",
        "through", "results", "research", "paper", "study"
    }

    counter = Counter(
        word for word in all_words
        if word not in stopwords
    )

    return [word for word, _ in counter.most_common(top_n)]


# ============================================================
# LITERATURE REVIEW
# ============================================================

def generate_literature_review(topic, papers):

    if not papers:
        return (
            f"Existing research related to {topic} indicates the "
            f"importance of developing data-driven and intelligent "
            f"solutions for this domain."
        )

    sections = []

    for i, paper in enumerate(papers, 1):

        title = get_title(paper)
        year = get_year(paper)
        abstract = get_abstract(paper)

        if abstract:
            summary = limit_text(abstract, 650)
        else:
            summary = (
                f"The study investigates approaches related to "
                f"{topic}."
            )

        sections.append(
            f"Paper {i}: {title} ({year}). {summary}"
        )

    return "\n\n".join(sections)


# ============================================================
# RESEARCH GAP
# ============================================================

def generate_research_gap(topic, papers):

    domain = get_topic_domain(topic)
    keywords = extract_common_keywords(topic, papers)

    common = ", ".join(keywords[:6])

    return (
        f"Based on the reviewed research papers, existing work in "
        f"{domain} mainly focuses on individual aspects of the "
        f"problem such as data collection, prediction, classification, "
        f"monitoring, or recommendation. However, there is an "
        f"opportunity to integrate multiple stages into a unified "
        f"intelligent system specifically designed for {topic}. "
        f"The reviewed literature highlights concepts including "
        f"{common if common else 'data analysis, intelligent processing and system automation'}. "
        f"The proposed research therefore focuses on combining "
        f"topic-specific data acquisition, NLP/AI-based processing, "
        f"decision generation and user-oriented output in one system."
    )


# ============================================================
# NLP TECHNIQUES
# ============================================================

def generate_nlp_section(topic):

    domain = get_topic_domain(topic)

    return (
        f"For the proposed {topic}, Natural Language Processing "
        f"techniques are used to process and analyze textual research "
        f"information related to {domain}. The system performs text "
        f"cleaning, keyword extraction, frequency analysis and "
        f"similarity analysis. TF-IDF and cosine similarity can be "
        f"used to compare documents, while keyword and phrase "
        f"extraction helps identify important concepts from the "
        f"retrieved literature."
    )


# ============================================================
# DATASET / SOURCE
# ============================================================

def generate_dataset_section(topic, papers):

    return (
        f"The primary research source for the proposed {topic} is "
        f"a collection of relevant research papers retrieved "
        f"automatically from academic literature sources. The system "
        f"uses the retrieved paper titles, abstracts, authors, "
        f"publication years and available full-text information. "
        f"These documents form the literature dataset used for "
        f"keyword extraction, comparison, research-gap identification "
        f"and research-paper synthesis. {len(papers)} research papers "
        f"were selected for the current synthesis."
    )


# ============================================================
# PROPOSED METHODOLOGY
# ============================================================

def generate_methodology_section(topic, papers):

    keywords = extract_common_keywords(topic, papers)

    common = ", ".join(keywords[:8])

    return (
        f"The proposed methodology for {topic} consists of several "
        f"integrated stages. First, the user provides the research "
        f"topic. The system automatically retrieves relevant research "
        f"papers. The retrieved documents are then processed to "
        f"extract titles, abstracts, keywords, methodologies, results "
        f"and limitations. NLP preprocessing is applied to clean and "
        f"normalize the text. TF-IDF, cosine similarity, keyword "
        f"frequency and n-gram analysis are used to compare the "
        f"literature. Important concepts identified from the reviewed "
        f"papers include {common if common else 'topic-specific features, methods and results'}. "
        f"The system then identifies common limitations and research "
        f"gaps. Finally, the extracted evidence is synthesized into "
        f"an original research paper specifically focused on {topic}, "
        f"with appropriate references to the reviewed studies."
    )


# ============================================================
# SYSTEM ARCHITECTURE
# ============================================================

def generate_architecture(topic):

    domain = get_topic_domain(topic)

    return f"""
User
  |
  v
Enter Research Topic
  |
  v
Academic Paper Search
  |
  v
Retrieve Relevant Research Papers
  |
  v
PDF / Abstract Extraction
  |
  v
NLP Processing
  |
  +--> Text Cleaning
  |
  +--> Keyword Extraction
  |
  +--> TF-IDF Analysis
  |
  +--> Similarity Analysis
  |
  +--> Important Information Extraction
  |
  v
Literature Comparison
  |
  v
Research Gap Identification
  |
  v
Dynamic Synthesis Engine
  |
  v
{topic}
Specific Research Paper
  |
  +--> Introduction
  +--> Literature Review
  +--> NLP Techniques
  +--> Methodology
  +--> Results
  +--> Applications
  +--> Limitations
  +--> Future Scope
  +--> Conclusion
  +--> References
"""


# ============================================================
# SYSTEM WORKFLOW
# ============================================================

def generate_workflow(topic):

    domain = get_topic_domain(topic)

    return f"""
DYNAMIC WORKFLOW FOR: {topic}

1. USER INPUT
   User enters the research topic:
   "{topic}"

2. TOPIC ANALYSIS
   The system identifies the major keywords and domain:
   {domain}

3. RESEARCH PAPER SEARCH
   The system searches academic literature and retrieves
   relevant research papers.

4. PAPER SELECTION
   The most relevant papers are selected for further analysis.

5. TEXT EXTRACTION
   Available abstracts and PDF text are extracted.

6. NLP PREPROCESSING
   Text cleaning, normalization, keyword extraction and
   important phrase identification are performed.

7. LITERATURE ANALYSIS
   The system analyzes methods, findings, results and
   limitations reported in the selected studies.

8. SIMILARITY ANALYSIS
   TF-IDF, cosine similarity, word overlap and n-gram
   similarity are used to compare the generated content
   with source literature.

9. RESEARCH GAP IDENTIFICATION
   Common limitations and missing aspects in the reviewed
   literature are analyzed.

10. DYNAMIC CONTENT GENERATION
    The system generates methodology, architecture,
    applications, advantages, limitations and future scope
    specifically for "{topic}".

11. RESEARCH PAPER SYNTHESIS
    Introduction, literature review, research gap,
    methodology, results, conclusion and references are
    combined into a new research-paper draft.

12. SIMILARITY VERIFICATION
    The generated paper is checked for textual similarity.

13. FINAL OUTPUT
    The system displays the synthesized research paper,
    references and analysis results for the user.
"""


# ============================================================
# RESULTS
# ============================================================

def generate_results_section(topic, papers):

    return (
        f"The proposed NLP-based research assistant generates a "
        f"topic-specific research output for {topic}. The system "
        f"automatically processes the retrieved literature and "
        f"extracts important concepts, research methods, findings "
        f"and limitations. The analysis provides a structured view "
        f"of the existing research and identifies potential gaps. "
        f"The final output is synthesized from {len(papers)} "
        f"retrieved research papers and includes references to "
        f"the source studies."
    )


# ============================================================
# APPLICATIONS
# ============================================================

def generate_applications(topic):

    domain = get_topic_domain(topic)

    return (
        f"The proposed system can be applied in {domain}. It can "
        f"support students, researchers and project developers by "
        f"automatically organizing research literature, identifying "
        f"important findings and generating a structured research "
        f"draft for {topic}. The system can also reduce the manual "
        f"effort required for initial literature exploration."
    )


# ============================================================
# ADVANTAGES
# ============================================================

def generate_advantages(topic):

    return (
        f"The major advantages of the proposed {topic} research "
        f"assistant include automated literature retrieval, reduced "
        f"manual searching effort, NLP-based document analysis, "
        f"automatic keyword extraction, research-gap identification, "
        f"structured paper generation, similarity verification and "
        f"topic-specific output generation."
    )


# ============================================================
# LIMITATIONS
# ============================================================

def generate_limitations(topic):

    return (
        f"The proposed system for {topic} has some limitations. "
        f"The quality of the generated research content depends on "
        f"the availability and quality of retrieved papers. PDF "
        f"extraction may be incomplete for scanned or protected "
        f"documents. Lexical similarity methods may not detect every "
        f"type of semantic similarity. Therefore, generated content "
        f"should be reviewed by the researcher before academic use."
    )


# ============================================================
# FUTURE SCOPE
# ============================================================

def generate_future_scope(topic):

    return (
        f"Future development of the {topic} research assistant can "
        f"include semantic embeddings, transformer-based NLP models, "
        f"improved academic paper ranking, automatic section-level "
        f"paper extraction, multilingual research analysis, "
        f"citation recommendation, stronger semantic similarity "
        f"checking and integration with additional academic databases."
    )


# ============================================================
# CONCLUSION
# ============================================================

def generate_conclusion(topic, papers):

    return (
        f"This work presents an NLP-based AI research assistant for "
        f"{topic}. The system combines automatic literature retrieval, "
        f"text extraction, NLP analysis, similarity measurement, "
        f"research-gap identification and dynamic research-paper "
        f"synthesis. By analyzing {len(papers)} relevant research "
        f"papers, the system provides a structured and topic-specific "
        f"research output. The approach can assist researchers in "
        f"understanding existing literature and developing new "
        f"research directions while maintaining appropriate "
        f"references to the reviewed sources."
    )


# ============================================================
# REFERENCES
# ============================================================

def generate_references(papers):

    references = []

    for i, paper in enumerate(papers, 1):

        authors = get_authors(paper)
        title = get_title(paper)
        year = get_year(paper)
        doi = paper.get("doi", "")

        reference = f"[{i}] {authors}. \"{title}\". {year}."

        if doi and doi != "N/A":
            reference += f" DOI: {doi}"

        references.append(reference)

    return "\n".join(references)


# ============================================================
# COMPLETE PAPER GENERATION
# ============================================================

def generate_paper(topic, papers):

    relevant_papers = get_relevant_papers(
        topic,
        papers,
        count=5
    )

    literature_review = generate_literature_review(
        topic,
        relevant_papers
    )

    research_gap = generate_research_gap(
        topic,
        relevant_papers
    )

    dataset = generate_dataset_section(
        topic,
        relevant_papers
    )

    nlp_section = generate_nlp_section(topic)

    methodology = generate_methodology_section(
        topic,
        relevant_papers
    )

    architecture = generate_architecture(topic)

    results = generate_results_section(
        topic,
        relevant_papers
    )

    applications = generate_applications(topic)

    advantages = generate_advantages(topic)

    limitations = generate_limitations(topic)

    future_scope = generate_future_scope(topic)

    conclusion = generate_conclusion(
        topic,
        relevant_papers
    )

    references = generate_references(
        relevant_papers
    )

    paper = f"""
# {topic}

## Abstract

This research presents an NLP-based AI Research Assistant
designed to support automated literature analysis and research
paper synthesis for {topic}. The system retrieves relevant
research papers, extracts useful information, applies NLP
techniques and identifies research gaps. The analyzed literature
is then used to generate a structured and topic-specific research
paper with references.

## 1. Introduction

Research in {topic} requires systematic study of existing
literature, identification of important methods and understanding
of limitations in previous work. Manual literature analysis can
require significant time and effort. The proposed AI Research
Assistant addresses this challenge by automatically retrieving
relevant studies and applying NLP techniques to organize and
analyze their content.

## 2. Literature Review

{literature_review}

## 3. Research Gap

{research_gap}

## 4. Dataset / Source of Data

{dataset}

## 5. NLP Techniques Used

{nlp_section}

## 6. Proposed Methodology

{methodology}

## 7. System Architecture

{architecture}

## 8. System Workflow

{generate_workflow(topic)}

## 9. Results and Expected Output

{results}

## 10. Applications

{applications}

## 11. Advantages

{advantages}

## 12. Limitations

{limitations}

## 13. Future Scope

{future_scope}

## 14. Conclusion

{conclusion}

## References

{references}
"""

    return paper.strip()
