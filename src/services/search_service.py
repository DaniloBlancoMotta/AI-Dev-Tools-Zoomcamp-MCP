import os
import requests
import zipfile
from typing import List, Dict, Any
from src.infra import minsearch
from src.core.interfaces import SearchServiceInterface

class FastMCPSearchService(SearchServiceInterface):
    def __init__(self, zip_url: str, zip_filename: str):
        self.zip_url = zip_url
        self.zip_filename = zip_filename
        self._index = None

    def _get_index(self):
        if self._index is not None:
            return self._index
        
        if not os.path.exists(self.zip_filename):
            response = requests.get(self.zip_url, verify=False)
            response.raise_for_status()
            with open(self.zip_filename, 'wb') as f:
                f.write(response.content)

        documents = []
        with zipfile.ZipFile(self.zip_filename, 'r') as z:
            for member in z.infolist():
                if not member.is_dir() and (member.filename.endswith('.md') or member.filename.endswith('.mdx')):
                    parts = member.filename.split('/')
                    clean_filename = '/'.join(parts[1:])
                    if not clean_filename: continue
                    with z.open(member) as f:
                        content = f.read().decode('utf-8')
                        documents.append({"filename": clean_filename, "content": content})

        self._index = minsearch.Index(text_fields=["content"], keyword_fields=["filename"])
        self._index.fit(documents)
        return self._index

    def search(self, query: str, num_results: int = 5) -> List[Dict[str, Any]]:
        idx = self._get_index()
        return idx.search(query=query, num_results=num_results)
