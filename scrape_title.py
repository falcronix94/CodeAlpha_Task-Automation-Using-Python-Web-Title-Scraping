import requests
import re
import os
from datetime import datetime

def fetch_title(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text

        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if title_match:
            return title_match.group(1).strip()
        else:
            return "No <title> tag found"
    except Exception as e:
        return f"Error: {e}"

def save_titles(results):
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join("output", f"titles_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        for url, title in results:
            f.write(f"URL: {url}\nTitle: {title}\n\n")

    print(f"Titles saved to {filename}")

if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.nytimes.com",
        "https://www.bbc.com",
        "https://www.coursera.org",
        "https://www.medium.com",
        "https://www.reddit.com",
        "https://www.w3schools.com"
    ]

    print("Scraping titles from 10 websites...\n")
    results = []

    for url in urls:
        print(f"{url}")
        title = fetch_title(url)
        print(f"{title}\n")
        results.append((url, title))

    save_titles(results)