# Application-Based Mini Project – NLP Research Assistant

## 1. Title of the Application-Based Mini Project

**NLP Research Assistant – Dynamic Topic-Based Research Paper Generation and Similarity Checking System**

---

## 2. Student Name and Roll Number

**Student Name:** Sejal Shastrakar
**Roll Number:** *BT240052ET*

---

## 3. Problem Statement / Objective

### Problem Statement

Students and researchers often spend a significant amount of time searching for information, organizing research content, preparing literature reviews, and structuring research papers. It can also be difficult to identify whether the generated content has a high similarity with existing documents.

### Objective

The objective of this project is to develop an **NLP-based Research Assistant** that can:

* Accept any research topic from the user.
* Automatically identify the research domain.
* Generate a structured research paper.
* Generate sections such as Abstract, Introduction, Literature Review, Research Gap, Methodology, Results, Applications, and Conclusion.
* Generate topic-specific keywords and references.
* Allow the user to upload a research paper.
* Analyze the uploaded paper using Copyleaks.
* Display the similarity score.
* Allow downloading when the similarity score is below 10%.
* Generate a new research paper when the similarity score is 10% or above.

---

## 4. Introduction

Natural Language Processing (NLP) is a branch of Artificial Intelligence that enables computers to understand, process, and generate human language.

The **NLP Research Assistant** is an application-based mini project that uses NLP and text-generation techniques to assist students in preparing research papers. The system accepts a research topic as input and dynamically generates content according to the selected topic.

The application provides a structured research-paper format consisting of multiple sections. It also provides a similarity-checking facility using Copyleaks. The user can upload the generated or existing research paper and analyze its similarity score.

The overall workflow is:

```text
Enter Research Topic
        ↓
Generate Research Paper
        ↓
Download / Check Paper
        ↓
Upload Paper
        ↓
Analyze with Copyleaks
        ↓
Get Similarity Score
        ↓
     ┌───────────────┐
     │ Similarity    │
     │ Score         │
     └───────┬───────┘
             ↓
       ┌─────┴─────┐
       ↓           ↓
     < 10%       ≥ 10%
       ↓           ↓
   Download     Generate
     Paper      New Paper
                   ↓
              Check Again
```

---

## 5. NLP Technique / Method Used

The project uses several NLP and text-processing concepts.

### Main Techniques

1. **Text Processing**

   * Processing research-topic text.
   * Organizing generated textual information.

2. **Topic Classification / Domain Detection**

   * The entered topic is analyzed to identify its research domain.

3. **Keyword Extraction**

   * Important keywords related to the research topic are generated.

4. **Natural Language Generation**

   * Research-paper sections are dynamically generated based on the user's topic.

5. **Text Similarity Checking**

   * The uploaded research paper is submitted to Copyleaks for similarity analysis.

6. **Content Structuring**

   * Generated information is organized into predefined research-paper sections.

7. **Document Text Extraction**

   * Text can be extracted from TXT, PDF, and DOCX files before analysis.

---

## 6. Dataset / Source of Data

This project does not require a fixed dataset for generating the research paper.

The system uses:

* User-entered research topics.
* Research information used by the application's generation module.
* Generated textual content.
* User-uploaded research papers.
* Copyleaks similarity-analysis results.

### Supported Input Documents

* `.txt`
* `.pdf`
* `.docx`

The uploaded document is converted into text before being submitted for similarity analysis.

---

## 7. Software / Tools / Libraries Used

### Software

* Python
* Visual Studio Code
* Streamlit
* Web Browser

### Python Libraries

```text
streamlit
python-dotenv
copyleaks
python-docx
pypdf
```

### Technologies

* Python
* NLP
* Artificial Intelligence
* Natural Language Generation
* Text Processing
* Similarity Detection

### External Service

**Copyleaks API** is used for similarity checking of the uploaded research paper.

---

## 8. Methodology / Workflow

### Step 1 – Enter Research Topic

The user enters any research topic into the application.

Example:

```text
AI Based E-Learning Recommendation System
```

### Step 2 – Generate Research Paper

The system processes the topic and dynamically generates a research paper.

The generated paper contains:

* Title
* Research Domain
* Keywords
* Abstract
* Introduction
* Topic Description
* Research Gap
* Literature Review
* Dataset / Research Data
* NLP / Data Processing Techniques
* Proposed Methodology
* System Architecture
* System Workflow
* Expected Results
* Applications
* Advantages
* Limitations
* Future Scope
* Conclusion
* References

### Step 3 – Check Paper

The user selects:

```text
Check Paper with Copyleaks
```

### Step 4 – Upload Paper

The user uploads a research paper in:

```text
TXT / PDF / DOCX
```

### Step 5 – Analyze

The uploaded document is converted into text and submitted to Copyleaks.

### Step 6 – Similarity Score

The application receives the similarity result and displays the percentage.

Example:

```text
Copyleaks Similarity Score: 7.50%
```

### Step 7 – Decision

If:

```text
Similarity < 10%
```

the paper passes the similarity requirement and the download option is provided.

If:

```text
Similarity ≥ 10%
```

the application asks the user to generate a new research paper and check it again.

---

## 9. Steps to Execute the Program / Project

### Step 1 – Open Project Folder

Open the project folder in **Visual Studio Code**.

### Step 2 – Open Terminal

Open:

```text
Terminal → New Terminal
```

### Step 3 – Create Virtual Environment

```bash
python -m venv venv
```

### Step 4 – Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5 – Install Required Libraries

```bash
pip install streamlit python-dotenv copyleaks python-docx pypdf
```

### Step 6 – Configure `.env`

Create a `.env` file in the project folder.

Add the required Copyleaks credentials:

```env
COPYLEAKS_EMAIL=your_email
COPYLEAKS_API_KEY=your_api_key
```

### Step 7 – Run the Application

```bash
streamlit run app.py
```

If the above command does not work:

```bash
python -m streamlit run app.py
```

### Step 8 – Open the Application

Streamlit will display a local address such as:

```text
http://localhost:8501
```

Open this address in a web browser.

---

## 10. Sample Input

### Research Topic

```text
AI Based E-Learning Recommendation System
```

### Sample Uploaded Paper

```text
AI Based E-Learning Recommendation System

This research focuses on the use of artificial intelligence
and natural language processing for recommending suitable
learning resources to students...
```

---

## 11. Sample Output

### Generated Paper

```text
Research Topic:
AI Based E-Learning Recommendation System

Domain:
Artificial Intelligence / Natural Language Processing

Keywords:
Artificial Intelligence
E-Learning
Recommendation System
Machine Learning
Natural Language Processing
```

The application generates sections such as:

```text
Abstract
Introduction
Topic Description
Research Gap
Literature Review
Dataset / Research Data
NLP Techniques
Proposed Methodology
System Architecture
System Workflow
Expected Results
Applications
Advantages
Limitations
Future Scope
Conclusion
References
```

### Similarity Output

Example:

```text
Copyleaks Analysis Completed

Similarity Score: 7.50%

Similarity score is below 10%.
The paper can now be downloaded.
```

For a higher score:

```text
Copyleaks Similarity Score: 15.20%

Similarity score is 10% or above.

Generate New Research Paper
```

---

## 12. Results / Observations

The developed application successfully provides a dynamic research-paper generation interface.

### Observations

* The user can enter different research topics.
* The system generates topic-specific research content.
* The generated paper is divided into structured sections.
* Keywords and research-domain information are provided.
* TXT, PDF, and DOCX files can be uploaded.
* Uploaded documents can be converted into text.
* Copyleaks can be used to analyze similarity.
* The similarity percentage is displayed in the application.
* Papers satisfying the configured similarity threshold can be downloaded.
* Papers with a similarity score of 10% or above can be regenerated and checked again.

---

## 13. Conclusion

The **NLP Research Assistant** demonstrates how Natural Language Processing and Artificial Intelligence can be applied to assist students in research-paper preparation.

The system provides a complete workflow from entering a research topic to generating structured research content and checking the uploaded paper for similarity.

The application reduces the manual effort involved in organizing research content and provides an easy-to-use interface for students. The similarity-checking stage also helps users identify when a paper needs further regeneration or revision.

Thus, the project demonstrates a practical application of **NLP, AI-based text generation, document processing, and text similarity analysis** in academic research assistance.

---

## 14. Resources / References

1. Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, Pearson.

2. Manning, C. D., Raghavan, P., and Schütze, H., *Introduction to Information Retrieval*, Cambridge University Press.

3. Python Documentation – Python programming language documentation.

4. Streamlit Documentation – Framework for developing Python-based data applications.

5. Copyleaks Documentation – API and similarity-analysis documentation.

6. Natural Language Processing concepts and academic research resources.

7. Research papers and publicly available resources related to Artificial Intelligence, NLP, recommendation systems, and text processing.

---

## Project Workflow Summary

```text
                ┌──────────────────────┐
                │   Enter Topic        │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Generate Paper       │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Check with Copyleaks │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Upload Paper         │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Analyze Paper        │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Similarity Score     │
                └──────────┬───────────┘
                           ↓
                 ┌─────────┴─────────┐
                 ↓                   ↓
              < 10%                ≥ 10%
                 ↓                   ↓
          Download Paper       Generate New Paper
                                     ↓
                                Check Again
```

---

## Project Files

```text
NLP_RESEARCH_ASSISTANT/
│
├── app.py
├── synthesis.py
├── copyleaks_checker.py
├── .env
├── requirements.txt
└── README.md
```
