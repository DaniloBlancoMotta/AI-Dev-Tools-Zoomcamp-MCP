import os
import zipfile

def check_counts():
    zip_filename = "fastmcp.zip"
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
                
                if clean_filename in ["README.md", "docs/servers/context.mdx", "examples/testing_demo/README.md", "docs/python-sdk/fastmcp-settings.mdx", "examples/fastmcp_config_demo/README.md"]:
                    with z.open(member) as f:
                        raw_content = f.read().decode('utf-8')
                        content = raw_content.lower()
                        count = content.count("demo")
                        length = len(raw_content)
                        print(f"{clean_filename}: count={count}, length={length}")

if __name__ == "__main__":
    check_counts()
