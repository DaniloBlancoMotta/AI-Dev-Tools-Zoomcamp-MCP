import os
import requests
import zipfile
import io
import minsearch
import urllib3

# Disable SSL warnings for the environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_and_index():
    zip_url = "https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip"
    zip_filename = "fastmcp.zip"
    
    # 1. Download if not already downloaded
    if not os.path.exists(zip_filename):
        print(f"Downloading {zip_url}...")
        response = requests.get(zip_url, verify=False)
        response.raise_for_status()
        with open(zip_filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f"{zip_filename} already exists.")

    # 2. Iterate over zip and read md/mdx
    documents = []
    with zipfile.ZipFile(zip_filename, 'r') as z:
        for member in z.infolist():
            if not member.is_dir() and (member.filename.endswith('.md') or member.filename.endswith('.mdx')):
                # 3. Remove first part of the path
                # Example: "fastmcp-main/docs/welcome.mdx" -> "docs/welcome.mdx"
                parts = member.filename.split('/')
                clean_filename = '/'.join(parts[1:])
                
                if not clean_filename: # Skip the top-level directory if it was somehow included
                    continue
                    
                with z.open(member) as f:
                    content = f.read().decode('utf-8')
                    documents.append({
                        "filename": clean_filename,
                        "content": content
                    })

    # 4. Index with minsearch
    index = minsearch.Index(
        text_fields=["content"],
        keyword_fields=["filename"]
    )
    index.fit(documents)
    return index

def search(index, query):
    # 5. Search function retrieves 5 most relevant
    results = index.search(
        query=query,
        filter_dict={},
        boost_dict={"content": 1.0},
        num_results=5
    )
    return results

if __name__ == "__main__":
    idx = download_and_index()
    query = "demo"
    results = search(idx, query)
    
    if results:
        print(f"Top result for '{query}': {results[0]['filename']}")
        # Printing top 5 for clarity
        for i, res in enumerate(results):
            print(f"{i+1}. {res['filename']}")
    else:
        print("No results found.")
