import requests
import pymupdf


# ============================================================
# DOWNLOAD PDF
# ============================================================

def download_pdf(url, filename):

    try:

        response = requests.get(
            url,
            timeout=60,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code != 200:
            return False

        content_type = response.headers.get(
            "content-type",
            ""
        ).lower()

        content = response.content

        # Check whether downloaded file is actually a PDF
        if (
            "pdf" not in content_type
            and not content.startswith(b"%PDF")
        ):
            return False

        with open(
            filename,
            "wb"
        ) as file:

            file.write(content)

        return True

    except Exception:
        return False


# ============================================================
# EXTRACT TEXT FROM PDF
# ============================================================

def extract_pdf_text(filename):

    try:

        document = pymupdf.open(
            filename
        )

        text = ""

        for page in document:

            text += page.get_text()

        document.close()

        if not text.strip():
            return ""

        return text

    except Exception as error:

        return (
            f"PDF extraction error: {error}"
        )
