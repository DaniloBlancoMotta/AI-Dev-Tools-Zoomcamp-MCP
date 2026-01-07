import os
import zipfile
import minsearch

def test():
    zip_filename = "fastmcp.zip"
    documents = []
    
    if not os.path.exists(zip_filename):
        print("Zip file not found!")
        return

    with zipfile.ZipFile(zip_filename, 'r') as z:
        for member in z.infolist():
            if not member.is_dir() and (member.filename.endswith('.md') or member.filename.endswith('.mdx')):
                parts = member.filename.split('/')
                clean_filename = '/'.join(parts[1:])
                
                if not clean_filename:
                    continue
                    
                with z.open(member) as f:
                    content = f.read().decode('utf-8')
                    documents.append({
                        "filename": clean_filename,
                        "content": content
                    })

    index = minsearch.Index(
        text_fields=["content", "filename"],
        keyword_fields=[]
    )
    index.fit(documents)
    
    results = index.search(
        query="demo",
        filter_dict={},
        boost_dict={"content": 1.0},
        num_results=5
    )
    
    for i, res in enumerate(results):
        print(f"{i+1}. {res['filename']}")

if __name__ == "__main__":
    test()
