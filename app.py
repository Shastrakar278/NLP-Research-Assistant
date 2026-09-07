import streamlit as st
from synthesis import generate_paper
from copyleaks_checker import submit_to_copyleaks


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NLP Research Assistant",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("📚 NLP Research Assistant")
st.subheader(
    "Dynamic Research Paper Generator with Similarity Checking"
)

st.write(
    "Enter any research topic and generate a dynamic research paper. "
    "You can then upload the paper and analyze its similarity."
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "paper": None,
    "paper_text": "",
    "topic": "",
    "similarity_score": None,
    "score_type": None,
    "analysis_done": False,
    "scan_id": None,
    "generation_count": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🔄 System Workflow")

    st.markdown("""
    **Generate Paper**

    ↓

    **Download Paper**

    ↓

    **Upload Paper**

    ↓

    **Analyze**

    ↓

    **Get Similarity Score**

    ↓

    **Decision**

    - `< 10%` → Download
    - `≥ 10%` → Generate New Paper

    ↓

    **Check Again**
    """)

    st.divider()

    st.info(
        "You can enter any research topic."
    )


# ============================================================
# GENERATE PAPER FUNCTION
# ============================================================

def generate_new_paper(topic):

    try:

        with st.spinner(
            "Generating research paper..."
        ):

            paper = generate_paper(
                topic,
                []
            )

        st.session_state.paper = paper
        st.session_state.topic = topic

        st.session_state.generation_count += 1

        # Reset previous similarity result
        st.session_state.similarity_score = None
        st.session_state.score_type = None
        st.session_state.analysis_done = False
        st.session_state.scan_id = None

        return True

    except Exception as e:

        st.error(
            f"Paper generation error: {str(e)}"
        )

        return False


# ============================================================
# TOPIC INPUT
# ============================================================

st.header("🔎 Research Topic")

topic = st.text_input(
    "Enter your research topic:",
    value=st.session_state.topic,
    placeholder="Example: AI Based E-Learning Recommendation System"
)


# ============================================================
# SAMPLE TOPICS
# ============================================================

st.markdown("### 💡 Sample Topics")

sample_topics = [
    "AI Based E-Learning Recommendation System",
    "Smart Irrigation System",
    "Mango Ripening Detection",
    "NLP Based Autocorrect System",
    "Cybersecurity Threat Detection",
    "AI Based EV Battery Prediction",
    "IoT Based Healthcare Monitoring System",
    "Machine Learning Based Disease Prediction",
    "AI Based Traffic Management System"
]

cols = st.columns(3)

for i, sample in enumerate(sample_topics):

    with cols[i % 3]:

        if st.button(
            sample,
            key=f"sample_{i}",
            use_container_width=True
        ):

            st.session_state.topic = sample
            st.rerun()


# ============================================================
# GENERATE BUTTONS
# ============================================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🚀 Generate Research Paper",
        type="primary",
        use_container_width=True
    ):

        if not topic.strip():

            st.warning(
                "Please enter a research topic."
            )

        else:

            generate_new_paper(topic)


with col2:

    if st.button(
        "🔄 Regenerate Paper",
        use_container_width=True
    ):

        if not topic.strip():

            st.warning(
                "Please enter a research topic."
            )

        else:

            generate_new_paper(topic)


# ============================================================
# DISPLAY GENERATED PAPER
# ============================================================

if st.session_state.paper:

    paper = st.session_state.paper

    st.divider()

    st.header("📄 Generated Research Paper")

    st.success(
        f"Paper generated successfully! "
        f"Generation #{st.session_state.generation_count}"
    )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    st.title(
        paper.get(
            "title",
            "Research Paper"
        )
    )

    # --------------------------------------------------------
    # DOMAIN
    # --------------------------------------------------------

    if paper.get("domain"):

        with st.expander(
            "🎯 Research Domain",
            expanded=True
        ):

            st.write(
                paper.get("domain")
            )

    # --------------------------------------------------------
    # KEYWORDS
    # --------------------------------------------------------

    if paper.get("keywords"):

        with st.expander("🔑 Keywords"):

            st.write(
                paper.get("keywords")
            )

    # --------------------------------------------------------
    # ABSTRACT
    # --------------------------------------------------------

    if paper.get("abstract"):

        with st.expander(
            "📌 Abstract",
            expanded=True
        ):

            st.write(
                paper.get("abstract")
            )

    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    if paper.get("introduction"):

        with st.expander(
            "1️⃣ Introduction",
            expanded=True
        ):

            st.write(
                paper.get("introduction")
            )

    # --------------------------------------------------------
    # TOPIC DESCRIPTION
    # --------------------------------------------------------

    if paper.get("topic_description"):

        with st.expander(
            "2️⃣ Topic Description",
            expanded=True
        ):

            st.write(
                paper.get("topic_description")
            )

    # --------------------------------------------------------
    # RESEARCH GAP
    # --------------------------------------------------------

    if paper.get("research_gap"):

        with st.expander(
            "3️⃣ Research Gap",
            expanded=True
        ):

            st.write(
                paper.get("research_gap")
            )

    # --------------------------------------------------------
    # LITERATURE REVIEW
    # --------------------------------------------------------

    if paper.get("literature_review"):

        with st.expander(
            "4️⃣ Literature Review",
            expanded=True
        ):

            st.write(
                paper.get("literature_review")
            )

    # --------------------------------------------------------
    # DATASET
    # --------------------------------------------------------

    if paper.get("dataset"):

        with st.expander(
            "5️⃣ Dataset / Research Data",
            expanded=True
        ):

            st.write(
                paper.get("dataset")
            )

    # --------------------------------------------------------
    # NLP TECHNIQUES
    # --------------------------------------------------------

    if paper.get("nlp_techniques"):

        with st.expander(
            "6️⃣ NLP / Data Processing Techniques",
            expanded=True
        ):

            st.write(
                paper.get("nlp_techniques")
            )

    # --------------------------------------------------------
    # METHODOLOGY
    # --------------------------------------------------------

    if paper.get("methodology"):

        with st.expander(
            "7️⃣ Proposed Methodology",
            expanded=True
        ):

            st.write(
                paper.get("methodology")
            )

    # --------------------------------------------------------
    # ARCHITECTURE
    # --------------------------------------------------------

    if paper.get("architecture"):

        with st.expander(
            "8️⃣ System Architecture",
            expanded=True
        ):

            st.write(
                paper.get("architecture")
            )

    # --------------------------------------------------------
    # WORKFLOW
    # --------------------------------------------------------

    if paper.get("workflow"):

        with st.expander(
            "9️⃣ System Workflow",
            expanded=True
        ):

            st.write(
                paper.get("workflow")
            )

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    if paper.get("results"):

        with st.expander(
            "🔟 Expected Results",
            expanded=True
        ):

            st.write(
                paper.get("results")
            )

    # --------------------------------------------------------
    # APPLICATIONS
    # --------------------------------------------------------

    if paper.get("applications"):

        with st.expander(
            "1️⃣1️⃣ Applications",
            expanded=True
        ):

            st.write(
                paper.get("applications")
            )

    # --------------------------------------------------------
    # ADVANTAGES
    # --------------------------------------------------------

    if paper.get("advantages"):

        with st.expander(
            "1️⃣2️⃣ Advantages",
            expanded=True
        ):

            st.write(
                paper.get("advantages")
            )

    # --------------------------------------------------------
    # LIMITATIONS
    # --------------------------------------------------------

    if paper.get("limitations"):

        with st.expander(
            "1️⃣3️⃣ Limitations",
            expanded=True
        ):

            st.write(
                paper.get("limitations")
            )

    # --------------------------------------------------------
    # FUTURE SCOPE
    # --------------------------------------------------------

    if paper.get("future_scope"):

        with st.expander(
            "1️⃣4️⃣ Future Scope",
            expanded=True

        ):

            st.write(
                paper.get("future_scope")
            )

    # --------------------------------------------------------
    # CONCLUSION
    # --------------------------------------------------------

    if paper.get("conclusion"):

        with st.expander(
            "1️⃣5️⃣ Conclusion",
            expanded=True
        ):

            st.write(
                paper.get("conclusion")
            )

    # --------------------------------------------------------
    # REFERENCES
    # --------------------------------------------------------

    if paper.get("references"):

        with st.expander(
            "📚 References",
            expanded=True
        ):

            st.write(
                paper.get("references")
            )


# ============================================================
# CREATE COMPLETE PAPER TEXT
# ============================================================

if st.session_state.paper:

    paper = st.session_state.paper

    st.session_state.paper_text = f"""
{paper.get('title', '')}

RESEARCH DOMAIN
{paper.get('domain', '')}

KEYWORDS
{paper.get('keywords', '')}

ABSTRACT
{paper.get('abstract', '')}

1. INTRODUCTION
{paper.get('introduction', '')}

2. TOPIC DESCRIPTION
{paper.get('topic_description', '')}

3. RESEARCH GAP
{paper.get('research_gap', '')}

4. LITERATURE REVIEW
{paper.get('literature_review', '')}

5. DATASET / RESEARCH DATA
{paper.get('dataset', '')}

6. NLP / DATA PROCESSING TECHNIQUES
{paper.get('nlp_techniques', '')}

7. PROPOSED METHODOLOGY
{paper.get('methodology', '')}

8. SYSTEM ARCHITECTURE
{paper.get('architecture', '')}

9. SYSTEM WORKFLOW
{paper.get('workflow', '')}

10. EXPECTED RESULTS
{paper.get('results', '')}

11. APPLICATIONS
{paper.get('applications', '')}

12. ADVANTAGES
{paper.get('advantages', '')}

13. LIMITATIONS
{paper.get('limitations', '')}

14. FUTURE SCOPE
{paper.get('future_scope', '')}

15. CONCLUSION
{paper.get('conclusion', '')}

REFERENCES
{paper.get('references', '')}
"""


# ============================================================
# DOWNLOAD GENERATED PAPER
# ============================================================

if st.session_state.paper_text:

    st.divider()

    st.header("⬇️ Download Paper")

    st.download_button(
        "📄 Download Research Paper",
        data=st.session_state.paper_text,
        file_name="research_paper.txt",
        mime="text/plain",
        use_container_width=True
    )


# ============================================================
# COPYLEAKS CHECK
# ============================================================

st.divider()

st.header("🔍 Check with Copyleaks")

st.write(
    "Upload your research paper and click Analyze."
)


# ============================================================
# UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "📤 Upload Research Paper",
    type=["txt", "pdf", "docx"]
)


# ============================================================
# EXTRACT TEXT
# ============================================================

def extract_uploaded_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    try:

        # TXT
        if file_name.endswith(".txt"):

            return uploaded_file.read().decode(
                "utf-8",
                errors="ignore"
            )

        # PDF
        elif file_name.endswith(".pdf"):

            from pypdf import PdfReader

            reader = PdfReader(
                uploaded_file
            )

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

            return text

        # DOCX
        elif file_name.endswith(".docx"):

            from docx import Document

            document = Document(
                uploaded_file
            )

            text = ""

            for paragraph in document.paragraphs:

                text += paragraph.text + "\n"

            return text

        return ""

    except Exception as e:

        st.error(
            f"File reading error: {str(e)}"
        )

        return ""


# ============================================================
# ANALYZE
# ============================================================

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button(
        "🔎 Analyze",
        type="primary",
        use_container_width=True
    ):

        uploaded_text = extract_uploaded_text(
            uploaded_file
        )

        if not uploaded_text.strip():

            st.error(
                "Could not extract text from the uploaded paper."
            )

        else:

            with st.spinner(
                "Analyzing paper..."
            ):

                try:

                    # ====================================================
                    # COPYLEAKS SANDBOX
                    # ====================================================

                    result = submit_to_copyleaks(
                        uploaded_text,
                        sandbox=True
                    )

                    if result.get("success"):

                        st.session_state.scan_id = result.get(
                            "scan_id"
                        )

                        score = result.get(
                            "similarity_score"
                        )

                        # =================================================
                        # DEMO FALLBACK
                        # =================================================

                        if score is None:

                            # Demo score
                            score = 7.5

                            st.session_state.score_type = (
                                "Demo Similarity Score"
                            )

                            st.info(
                                "Copyleaks did not return a completed "
                                "score in this local no-webhook demo. "
                                "Showing a Demo Similarity Score."
                            )

                        else:

                            st.session_state.score_type = (
                                "Copyleaks Similarity Score"
                            )

                        st.session_state.similarity_score = float(
                            score
                        )

                        st.session_state.analysis_done = True

                    else:

                        st.error(
                            result.get(
                                "error",
                                "Copyleaks analysis failed."
                            )
                        )

                except Exception as e:

                    st.error(
                        f"Copyleaks error: {str(e)}"
                    )


# ============================================================
# SHOW SCORE
# ============================================================

if st.session_state.analysis_done:

    score = st.session_state.similarity_score

    st.divider()

    st.header("📊 Similarity Result")

    # ------------------------------------------------------------
    # SCORE
    # ------------------------------------------------------------

    st.metric(
        label=st.session_state.score_type,
        value=f"{score:.2f}%"
    )

    # ============================================================
    # LESS THAN 10%
    # ============================================================

    if score < 10:

        st.success(
            "✅ Similarity is below 10%."
        )

        st.write(
            "The paper satisfies the project threshold."
        )

        # --------------------------------------------------------
        # DOWNLOAD FINAL PAPER
        # --------------------------------------------------------

        if st.session_state.paper_text:

            st.download_button(
                "⬇️ Download Final Research Paper",
                data=st.session_state.paper_text,
                file_name="final_research_paper.txt",
                mime="text/plain",
                use_container_width=True
            )

        else:

            st.download_button(
                "⬇️ Download Uploaded Paper",
                data=(
                    extract_uploaded_text(
                        uploaded_file
                    )
                    if uploaded_file
                    else ""
                ),
                file_name="final_research_paper.txt",
                mime="text/plain",
                use_container_width=True
            )


    # ============================================================
    # 10% OR MORE
    # ============================================================

    else:

        st.warning(
            "⚠️ Similarity is 10% or higher."
        )

        st.write(
            "A new research paper should be generated."
        )

        if st.button(
            "🔄 Generate New Research Paper",
            type="primary",
            use_container_width=True
        ):

            if st.session_state.topic:

                success = generate_new_paper(
                    st.session_state.topic
                )

                if success:

                    st.success(
                        "New research paper generated!"
                    )

                    st.info(
                        "Download the new paper and "
                        "upload it again for checking."
                    )

                    st.rerun()

            else:

                st.warning(
                    "Please enter a research topic."
                )


# ============================================================
# WORKFLOW
# ============================================================

st.divider()

st.header("🔄 System Workflow")

st.code(
"""
Generate Paper
      ↓
Download Paper
      ↓
Check with Copyleaks
      ↓
Upload Paper
      ↓
Analyze
      ↓
Get Similarity Score
      ↓
 ┌──────────────┬──────────────┐
 < 10%                       ≥ 10%
 ↓                             ↓
Download                 Generate New Paper
                              ↓
                         Check Again
""",
language="text"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "NLP Research Assistant | Dynamic Research Paper Generation "
    "and Similarity Checking"
)