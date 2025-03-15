import os

def get_markdown_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.md') and f != 'README.md']

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_readme(content):
    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(content)

def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    markdown_files = get_markdown_files(directory)
    
    readme_content = "# Combined Markdown Files\n\n"
    for md_file in markdown_files:
        readme_content += f"## {md_file}\n\n"
        readme_content += read_file(os.path.join(directory, md_file)) + "\n\n"
    
    write_to_readme(readme_content)

if __name__ == "__main__":
    main()
