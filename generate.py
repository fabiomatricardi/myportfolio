import os
import yaml
import markdown
from jinja2 import Environment, FileSystemLoader

def parse_markdown_with_frontmatter(file_path):
    """
    Parses a markdown file containing optional YAML frontmatter.
    Returns a tuple: (metadata_dict, body_html_string)
    """
    if not os.path.exists(file_path):
        return {}, ""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file starts with YAML frontmatter markers
    if content.strip().startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1]) or {}
                body_md = parts[2].strip()
                body_html = markdown.markdown(body_md)
                return metadata, body_html
            except yaml.YAMLError as e:
                print(f"Error parsing YAML in {file_path}: {e}")
                
    # If no valid frontmatter is found, treat the entire file as body text
    return {}, markdown.markdown(content)

def parse_yaml_list(file_path):
    """Utility to parse lists directly from markdown files with YAML blocks."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = content.split('---')
    if len(parts) >= 3:
        return yaml.safe_load(parts[1]) or []
    return []

def main():
    # Setup template rendering environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    # 1. Parse Bio Markdown with metadata details
    bio_meta, bio_html = parse_markdown_with_frontmatter('content/bio.md')

    # 2. Parse structured lists (Experiences, Education, Portfolio)
    experiences = parse_yaml_list('content/experiences.md')
    education = parse_yaml_list('content/education.md')
    portfolio = parse_yaml_list('content/portfolio.md')

    # 3. Compile everything together
    output_html = template.render(
        bio_meta=bio_meta,
        bio_html=bio_html,
        experiences=experiences,
        education=education,
        portfolio=portfolio
    )

    # Output directly to the root as index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output_html)
    print("✓ Successfully generated index.html with integrated bio portrait layout.")

if __name__ == '__main__':
    main()