import requests


def reconstruct_abstract(inverted_index):

    if not inverted_index:
        return ""

    words = []

    for word, positions in inverted_index.items():

        for position in positions:
            words.append((position, word))

    words.sort()

    return " ".join(
        word for _, word in words
    )


def search_papers(topic, count=5):

    url = "https://api.openalex.org/works"

    params = {
        "search": topic,
        "per-page": count,
        "sort": "relevance_score:desc"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    papers = []

    for item in data.get("results", []):

        authors = []

        for author in item.get("authorships", []):

            name = author.get(
                "author", {}
            ).get(
                "display_name"
            )

            if name:
                authors.append(name)

        abstract = reconstruct_abstract(
            item.get(
                "abstract_inverted_index"
            )
        )

        pdf_url = None

        best_oa = item.get(
            "best_oa_location"
        )

        if best_oa:

            pdf_url = best_oa.get(
                "pdf_url"
            )

        primary_location = item.get(
            "primary_location"
        )

        if not pdf_url and primary_location:

            pdf_url = primary_location.get(
                "pdf_url"
            )

        journal = "N/A"

        if primary_location:

            source = primary_location.get(
                "source"
            )

            if source:

                journal = source.get(
                    "display_name",
                    "N/A"
                )

        papers.append({

            "title": item.get(
                "title",
                "Unknown"
            ),

            "year": item.get(
                "publication_year",
                "N/A"
            ),

            "doi": item.get(
                "doi",
                "N/A"
            ),

            "authors": authors,

            "journal": journal,

            "abstract": abstract,

            "pdf_url": pdf_url,

            "openalex_id": item.get(
                "id",
                ""
            )
        })

    return papers
