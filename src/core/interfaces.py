from typing import Protocol, List, Dict, Any

class SearchServiceInterface(Protocol):
    def search(self, query: str, num_results: int = 5) -> List[Dict[str, Any]]:
        ...

class ScrapingServiceInterface(Protocol):
    def scrape(self, url: str) -> str:
        ...

class MathServiceInterface(Protocol):
    def add(self, a: int, b: int) -> int:
        ...

class UtilityServiceInterface(Protocol):
    def hash_text(self, text: str) -> str:
        ...
