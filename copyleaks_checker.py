import os
import base64
import uuid

from dotenv import load_dotenv

from copyleaks.copyleaks import Copyleaks
from copyleaks.models.submit.document import FileDocument
from copyleaks.models.submit.properties.scan_properties import ScanProperties


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

EMAIL = os.getenv("COPYLEAKS_EMAIL")
API_KEY = os.getenv("COPYLEAKS_API_KEY")


# ============================================================
# SUBMIT PAPER TO COPYLEAKS
# ============================================================

def submit_to_copyleaks(text):

    # Check credentials
    if not EMAIL or not API_KEY:

        return {
            "success": False,
            "message": "Copyleaks credentials are missing."
        }

    # Check input text
    if not text or not text.strip():

        return {
            "success": False,
            "message": "Research paper text is empty."
        }

    try:

        # ----------------------------------------------------
        # LOGIN TO COPYLEAKS
        # ----------------------------------------------------

        token = Copyleaks.login(
            EMAIL,
            API_KEY
        )

        # ----------------------------------------------------
        # CONVERT TEXT TO BASE64
        # ----------------------------------------------------

        encoded_text = base64.b64encode(
            text.encode("utf-8")
        ).decode("utf-8")

        # ----------------------------------------------------
        # CREATE UNIQUE SCAN ID
        # ----------------------------------------------------

        scan_id = (
            "research_"
            + uuid.uuid4().hex
        )

        # ----------------------------------------------------
        # SCAN PROPERTIES
        # ----------------------------------------------------

        properties = ScanProperties(
            "https://example.com/webhook/{STATUS}"
        )

        # Sandbox mode for testing
        properties.set_sandbox(True)

        # ----------------------------------------------------
        # CREATE DOCUMENT
        # ----------------------------------------------------

        document = FileDocument(
            encoded_text,
            "generated_research_paper.txt"
        )

        document.set_properties(
            properties
        )

        # ----------------------------------------------------
        # SUBMIT DOCUMENT
        # ----------------------------------------------------

        Copyleaks.submit_file(
            token,
            scan_id,
            document
        )

        # ----------------------------------------------------
        # RETURN RESULT
        # ----------------------------------------------------

        return {
            "success": True,
            "scan_id": scan_id,
            "message": "Research paper submitted successfully to Copyleaks."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }
