from fastmcp import FastMCP
import urllib3
from src.services.search_service import FastMCPSearchService
from src.services.scraping_service import JinaScrapingService
from src.services.utility_service import BasicUtilityService
from src.tools.registry import MCPToolRegistry

# Disable warnings for insecure requests (if needed for the zip download)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_app():
    # 1. Initialize FastMCP
    mcp = FastMCP("Demo")

    # 2. Initialize Services (Dependency Injection)
    search_service = FastMCPSearchService(
        zip_url="https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip",
        zip_filename="fastmcp.zip"
    )
    scraping_service = JinaScrapingService()
    utility_service = BasicUtilityService()

    # 3. Register Tools
    MCPToolRegistry(
        mcp=mcp,
        search_service=search_service,
        scraping_service=scraping_service,
        utility_service=utility_service
    )

    return mcp

if __name__ == "__main__":
    app = create_app()
    app.run()
