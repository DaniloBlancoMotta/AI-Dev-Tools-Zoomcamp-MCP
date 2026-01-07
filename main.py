from fastmcp import FastMCP
import os
import requests
import zipfile
import minsearch
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def hash_text(text: str) -> str:
    """Hash a string using SHA-256"""
    import hashlib
    return hashlib.sha256(text.encode()).hexdigest()

@mcp.tool
def scrape_page(url: str) -> str:
    """Scrape the content of a web page using Jina reader"""
    import requests
    jina_url = f"https://r.jina.ai/{url}"
    response = requests.get(jina_url)
    response.raise_for_status()
    return response.text

# --- Search Implementation for Question 6 ---
_index = None

def get_index():
    global _index
    if _index is not None:
        return _index
    
    zip_url = "https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip"
    zip_filename = "fastmcp.zip"
    
    if not os.path.exists(zip_filename):
        response = requests.get(zip_url, verify=False)
        response.raise_for_status()
        with open(zip_filename, 'wb') as f:
            f.write(response.content)

    documents = []
    with zipfile.ZipFile(zip_filename, 'r') as z:
        for member in z.infolist():
            if not member.is_dir() and (member.filename.endswith('.md') or member.filename.endswith('.mdx')):
                parts = member.filename.split('/')
                clean_filename = '/'.join(parts[1:])
                if not clean_filename: continue
                with z.open(member) as f:
                    content = f.read().decode('utf-8')
                    documents.append({"filename": clean_filename, "content": content})

    _index = minsearch.Index(text_fields=["content"], keyword_fields=["filename"])
    _index.fit(documents)
    return _index

@mcp.tool
def search_docs(query: str) -> str:
    """Search FastMCP documentation for a query"""
    idx = get_index()
    results = idx.search(query=query, num_results=5)
    
    output = []
    for res in results:
        output.append(f"File: {res['filename']}\nContent Preview: {res['content'][:200]}...")
    
    return "\n\n---\n\n".join(output)

if __name__ == "__main__":
    mcp.run()
