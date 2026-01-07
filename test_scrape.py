import requests

def test_scrape():
    url = "https://github.com/alexeygrigorev/minsearch"
    jina_url = f"https://r.jina.ai/{url}"
    print(f"Scraping {jina_url}...")
    response = requests.get(jina_url)
    response.raise_for_status()
    content = response.text
    print(f"Character count: {len(content)}")

if __name__ == "__main__":
    test_scrape()
