import requests
from src.core.interfaces import ScrapingServiceInterface

class JinaScrapingService(ScrapingServiceInterface):
    def __init__(self, base_url: str = "https://r.jina.ai/"):
        self.base_url = base_url

    def scrape(self, url: str) -> str:
        jina_url = f"{self.base_url}{url}"
        response = requests.get(jina_url)
        response.raise_for_status()
        return response.text
