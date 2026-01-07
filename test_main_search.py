from main import get_index

def test_tool_logic():
    print("Initializing index...")
    idx = get_index()
    query = "resources"
    print(f"Searching for: {query}")
    results = idx.search(query=query, num_results=5)
    
    for i, res in enumerate(results):
        print(f"\n{i+1}. File: {res['filename']}")
        print(f"Preview: {res['content'][:150].replace('\n', ' ')}...")

if __name__ == "__main__":
    test_tool_logic()
