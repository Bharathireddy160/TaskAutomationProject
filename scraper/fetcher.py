import requests
from bs4 import BeautifulSoup


def get_website_title(url):

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        if soup.title:
            return soup.title.string.strip()

        return "No title found"

    except Exception as e:
        print("Error:", e)
        return None