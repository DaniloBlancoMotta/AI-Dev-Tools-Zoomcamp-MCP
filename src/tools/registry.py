from fastmcp import FastMCP
from src.core.interfaces import (
    SearchServiceInterface, 
    ScrapingServiceInterface, 
    MathServiceInterface, 
    UtilityServiceInterface
)

class MCPToolRegistry:
    def __init__(
        self, 
        mcp: FastMCP,
        search_service: SearchServiceInterface,
        scraping_service: ScrapingServiceInterface,
        utility_service: MathServiceInterface # Combined math/utility for brevity
    ):
        self.mcp = mcp
        self.search_service = search_service
        self.scraping_service = scraping_service
        self.utility_service = utility_service
        self._register_tools()

    def _register_tools(self):
        @self.mcp.tool
        def add(a: int, b: int) -> int:
            """Add two numbers"""
            return self.utility_service.add(a, b)

        @self.mcp.tool
        def hash_text(text: str) -> str:
            """Hash a string using SHA-256"""
            return self.utility_service.hash_text(text)

        @self.mcp.tool
        def scrape_page(url: str) -> str:
            """Scrape the content of a web page using Jina reader"""
            return self.scraping_service.scrape(url)

        @self.mcp.tool
        def search_docs(query: str) -> str:
            """Search FastMCP documentation for a query"""
            results = self.search_service.search(query=query, num_results=5)
            output = []
            for res in results:
                output.append(f"File: {res['filename']}\nContent Preview: {res['content'][:200]}...")
            return "\n\n---\n\n".join(output)
