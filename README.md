That **Claude Aesthetic** is an incredible choice. It strikes a beautiful balance between intellectual, literary depth (via the serif body font and organic cream tones) and modern, precise engineering (via the clean geometry, generous whitespace, and sharp terracotta accents). It feels premium, thoughtful, and highly intentional.

Now that we have the full picture—the **GitHub Actions engine**, the **single-page layout requirements**, and this **sophisticated visual style**—we are ready to construct the entire system.

Here is the complete blueprint, code, and workflow to get your automated portfolio live on GitHub Pages.

---

## 1. Repository Structure

To keep your workspace clean, organize your repository exactly like this:

```text
├── .github/
│   └── workflows/
│       └── deploy.yml          # The GitHub Actions automation script
├── content/
│   ├── bio.md                  # Your biography text
│   ├── education.md            # Your academic background
│   ├── experiences.md          # Your professional history
│   └── portfolio.md            # Your best articles (formatted for cards)
├── templates/
│   └── index.html              # The HTML/Jinja2 template with Claude styling
├── generate.py                 # The Python parsing script
├── requirements.txt            # Python dependencies
└── README.md

```

---

## 2. Content Modeling (The Markdown Files)

To make it easy for our Python script to parse your content into structured sections and cards, create your Markdown files inside the `content/` folder using the formats below.

### `content/bio.md`

```markdown
# Process Automation Engineer & AI Architect

I specialize in bridge-building between industrial engineering systems and local, privacy-focused AI environments. Based in Novara, Italy, I design intelligent structures that treat context as code.

```

### `content/experiences.md`

```markdown
---
- role: "Lead Automation & Systems Engineer"
  company: "Industrial Control Systems"
  duration: "2024 - Present"
  details: "Managing large-scale migrations of Emerson DeltaV control architectures across multi-site international environments including France and South Korea."
- role: "Technical Writer & Content Creator"
  company: "The OpenCode Revolution"
  duration: "2025 - Present"
  details: "Authoring deep-dives into Harness Engineering, local LLM architectures, and optimizing model performance on consumer hardware."
---

```

### `content/education.md`

```markdown
---
- degree: "B.Sc. in Industrial Engineering"
  institution: "Technical University"
  duration: "2019 - 2023"
  details: "Specialized in process control, automation loops, and computational systems logic."
---

```

### `content/portfolio.md`

```markdown
---
- title: "The OpenCode Revolution"
  description: "An in-depth manifesto on executing high-performance, 1-bit local LLMs on consumer-grade hardware and iGPUs."
  banner: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80"
  link: "https://github.com"
- title: "Harness Engineering vs Prompt Engineering"
  description: "Moving beyond fragile text prompts to building rigid context environments using Model Context Protocol (MCP)."
  banner: "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&w=800&q=80"
  link: "https://github.com"
---

```

---

## 3. The HTML Canvas (`templates/index.html`)

This template implements the **Claude Aesthetic** using standard Tailwind CSS mappings, Google Fonts integration for Poppins/Lora, and custom asymmetric layouts with load-in micro-animations.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ bio_meta.name or 'Portfolio' }} | {{ bio_meta.role or 'Systems Engineer' }}</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- Tailwind CSS Engine -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        pampas: '#F4F3EE',
                        charcoal: '#141413',
                        claudeOrange: '#C15F3C',
                        mutedBlue: '#6a9bcc',
                        mossGreen: '#788c5d'
                    },
                    fontFamily: {
                        sans: ['Poppins', 'sans-serif'],
                        serif: ['Lora', 'serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Lora', serif; background-color: #F4F3EE; color: #141413; }
        h1, h2, h3, h4 { font-family: 'Poppins', sans-serif; }
        
        /* Interactive micro-motions */
        @keyframes revealUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-reveal { animation: revealUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; }
        .delay-1 { animation-delay: 150ms; }
        .delay-2 { animation-delay: 300ms; }
    </style>
</head>
<body class="bg-pampas text-charcoal selection:bg-claudeOrange selection:text-white antialiased min-h-screen">

    <!-- Hero / Profile Header Section -->
    <header class="max-w-6xl mx-auto px-6 pt-20 pb-16 md:pt-32 md:pb-24">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-16 items-center animate-reveal">
            
            <!-- Left Portrait Column (Asymmetrical sizing) -->
            {% if bio_meta.avatar %}
            <div class="md:col-span-4 flex justify-start">
                <div class="relative group max-w-[280px] w-full aspect-square">
                    <!-- Offset background design block to emphasize Claude style -->
                    <div class="absolute inset-0 border border-claudeOrange translate-x-4 translate-y-4 rounded-xl transition-transform duration-300 group-hover:translate-x-2 group-hover:translate-y-2"></div>
                    <div class="w-full h-full bg-charcoal rounded-xl overflow-hidden relative border border-charcoal/10">
                        <img 
                            src="{{ bio_meta.avatar }}" 
                            alt="{{ bio_meta.name }}" 
                            class="w-full h-full object-cover filter grayscale contrast-110 transition-all duration-500 ease-out group-hover:grayscale-0 group-hover:scale-105"
                        >
                    </div>
                </div>
            </div>
            {% endif %}

            <!-- Right Bio Text Column -->
            <div class="{% if bio_meta.avatar %}md:col-span-8{% else %}md:col-span-12{% endif %} space-y-4">
                <span class="text-claudeOrange font-sans uppercase tracking-widest text-xs font-semibold block">// System Profile Activated</span>
                <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-charcoal leading-none">
                    {{ bio_meta.name }}
                </h1>
                <p class="text-lg md:text-xl font-sans text-charcoal/60 font-medium">
                    {{ bio_meta.role }}
                </p>
                <div class="prose prose-lg font-serif text-charcoal leading-relaxed pt-2 max-w-3xl">
                    {{ bio_html }}
                </div>
            </div>

        </div>
    </header>

    <!-- Content Sections Matrix -->
    <main class="max-w-6xl mx-auto px-6 pb-24">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-start">
            
            <!-- Left Side: Experience & Education Timeline nodes -->
            <div class="lg:col-span-5 space-y-16 animate-reveal delay-1">
                
                <!-- Experience -->
                <section>
                    <h2 class="text-xs uppercase tracking-widest font-bold text-charcoal/40 border-b border-charcoal/10 pb-3 mb-6">Experience</h2>
                    <div class="space-y-8">
                        {% for exp in experiences %}
                        <div class="group">
                            <span class="text-xs font-sans text-mossGreen font-semibold block mb-1">{{ exp.duration }}</span>
                            <h3 class="text-lg font-bold font-sans tracking-tight text-charcoal group-hover:text-claudeOrange transition-colors duration-200">{{ exp.role }}</h3>
                            <p class="text-sm font-sans text-charcoal/50 mb-2">{{ exp.company }}</p>
                            <p class="text-sm text-charcoal/80 leading-relaxed font-serif">{{ exp.details }}</p>
                        </div>
                        {% endfor %}
                    </div>
                </section>

                <!-- Education -->
                <section>
                    <h2 class="text-xs uppercase tracking-widest font-bold text-charcoal/40 border-b border-charcoal/10 pb-3 mb-6">Education</h2>
                    <div class="space-y-8">
                        {% for edu in education %}
                        <div>
                            <span class="text-xs font-sans text-mutedBlue font-semibold block mb-1">{{ edu.duration }}</span>
                            <h3 class="text-md font-bold font-sans text-charcoal">{{ edu.degree }}</h3>
                            <p class="text-xs font-sans text-charcoal/50 mb-2">{{ edu.institution }}</p>
                            <p class="text-sm text-charcoal/80 font-serif">{{ edu.details }}</p>
                        </div>
                        {% endfor %}
                    </div>
                </section>

            </div>

            <!-- Right Side: Selected Portfolio Cards (Interactive highlight cards) -->
            <div class="lg:col-span-7 animate-reveal delay-2">
                <section>
                    <h2 class="text-xs uppercase tracking-widest font-bold text-charcoal/40 border-b border-charcoal/10 pb-3 mb-6">Selected Articles & Projects</h2>
                    <div class="grid grid-cols-1 gap-8">
                        {% for card in portfolio %}
                        <a href="{{ card.link }}" target="_blank" class="group block bg-white border border-charcoal/5 rounded-lg overflow-hidden transition-all duration-300 hover:border-claudeOrange/30 hover:shadow-xl hover:shadow-claudeOrange/5">
                            <div class="aspect-[16/7] w-full bg-pampas overflow-hidden relative">
                                <img src="{{ card.banner }}" alt="{{ card.title }}" class="w-full h-full object-cover filter grayscale contrast-115 mix-blend-multiply group-hover:grayscale-0 group-hover:scale-102 transition-all duration-500 ease-out">
                                <div class="absolute inset-0 bg-gradient-to-t from-charcoal/20 to-transparent mix-blend-multiply"></div>
                            </div>
                            <div class="p-6">
                                <h3 class="text-xl font-bold font-sans tracking-tight text-charcoal group-hover:text-claudeOrange transition-colors duration-200 flex items-center justify-between">
                                    {{ card.title }}
                                    <span class="text-claudeOrange opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-300 text-sm">→</span>
                                </h3>
                                <p class="mt-2 text-sm text-charcoal/70 font-serif leading-relaxed">{{ card.description }}</p>
                            </div>
                        </a>
                        {% endfor %}
                    </div>
                </section>
            </div>

        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-charcoal/5 max-w-6xl mx-auto px-6 py-12 text-center text-xs font-sans text-charcoal/40">
        Generated automatically via GitHub Actions • Built with Claude Aesthetic
    </footer>

</body>
</html>
```

---

## 4. The Python Generation Engine (`generate.py`)

This lightweight engine parses the standard Markdown from your bio, strips the YAML blocks out of your dynamic metadata lists, converts the text, and renders everything smoothly through Jinja2 templates.

First, set up your `requirements.txt`:

```text
markdown==3.6
PyYAML==6.0.1
Jinja2==3.1.4

```

Then create `generate.py`:

```python
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
```

---

## 5. The Automation Engine (`.github/workflows/deploy.yml`)

This configuration dictates the behavior of your GitHub Runner. Every time you issue a `git push` command containing updates to your articles or experience data, this runner spins up a minimal container, targets Python, runs your generator, and deploys the fresh webpage structure cleanly.

```yaml
name: Deploy Portfolio to GitHub Pages

on:
  push:
    branches:
      - main  # Set to master if your primary branch is master

permissions:
  contents: write

# Force the runner engine to use Node 24 directly to silence the deprecation logs
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: 'true'

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code Base
        uses: actions/checkout@v4

      - name: Set up Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          # We temporarily remove the strict cache parameter for the first setup run 
          # to clear the Cache 400 error block cleanly.

      - name: Install Generation Dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Compile HTML Site
        run: |
          python generate.py

      - name: Deploy Compiled index.html to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
          publish_branch: gh-pages
          keep_files: false
```

---

## 6. Going Live on GitHub

1. **Initialize Git Workspace:** Local Terminal.
Commit all file structures created across the steps above directly into your local folder workspace root:

```bash
git init
git add .
git commit -m "feat: infrastructure configuration for Claude Aesthetic portfolio"

```


2. **Configure GitHub Action Permissions:** GitHub Dashboard Browser.
Before pushing code, tell GitHub to allow your Workflow runner to write files back to the repository:

* Go to your repository on GitHub.
* Navigate to **Settings** → **Actions** → **General**.
* Scroll down to **Workflow permissions**.
* Select **Read and write permissions**, then hit **Save**.


3. **Push Code and Trigger Run:** Local Terminal.
Link your local workspace tracking architecture to your remote GitHub repository target destination and execute push operations:


`https://github.com/fabiomatricardi/myportfolio.git`


```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main

```


4. **Activate GitHub Pages Target Branch:** GitHub Dashboard Browser.
Once the initial Workflow runner completes execution successfully, a separate target infrastructure branch named `gh-pages` will exist:

* Head to your GitHub repository dashboard.
* Click **Settings** → **Pages**.
* Under **Build and deployment**, switch the source dropdown to **Deploy from a branch**.
* Select the newly created `gh-pages` branch, target the `/ (root)` folder directory, and save.


> your page will be published at an address like this.


[https://fabiomatricardi.github.io/myportfolio/](https://fabiomatricardi.github.io/myportfolio/)


---

```markdown
# 🏛️ Automated Portfolio Website (Claude Aesthetic)

A minimal, high-impact, single-page professional portfolio built specifically for GitHub Pages. This project implements a modern architectural separation of concerns: **content lives strictly as pure Markdown (`.md`) text files**, while an automated processing script handles formatting, structure rendering, and deployment hands-free.

Inspired by the **Claude Aesthetic**, the UI features an asymmetric layout built with elegant typography structures, generous whitespace metrics, editorial light/dark color block zones, and load-in micro-animations.

---

## 🛠️ System Architecture Diagram

```text
[ Push Changes to Main ] ────► Triggers GitHub Actions
                                         │
    ┌────────────────────────────────────┘
    ▼
[ Virtual Runner Container ]
    │
    ├── 1. Isolates Runtime Environment (Node 24 / Python 3.11)
    ├── 2. Parses Metadata Frontmatter & Text Content via Jinja2 & Markdown
    ├── 3. Compiles Clean Web Structure into local `/public` directory
    └── 4. Uses Secure GITHUB_TOKEN to force-deploy output to `gh-pages` branch

```

---

## 📂 Repository Layout

```text
├── .github/
│   └── workflows/
│       └── deploy.yml          # Fixed, warning-free GitHub Actions architecture
├── content/
│   ├── bio.md                  # Biography text file + portrait YAML metadata
│   ├── education.md            # Academic historical timeline parameters
│   ├── experiences.md          # Professional employment timelines 
│   └── portfolio.md            # Article cards configuration dataset (Title, Banner, Link)
├── templates/
│   └── index.html              # Core Jinja2 markup Canvas with Claude theme variables
├── generate.py                 # Core parsing engine script
└── requirements.txt            # Python processing dependencies

```

---

## 🎛️ Content Schema Formatting Laws

To prevent build compilation failures, the data parameters stored inside the `content/` Markdown files must conform to strict structural guidelines.

### Biography Configuration (`content/bio.md`)

Includes optional metadata frontmatter properties mapping your name, professional title, and portrait imagery:

```markdown
---
name: "Fabio Matricardi"
role: "Industrial Automation Engineer & Local AI Architect"
avatar: "[https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80](https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80)"
---
Your markdown-formatted biography goes here...

```

### Card Collections Formatting (`content/portfolio.md`)

> ⚠️ **CRITICAL LOGIC:** YAML arrays are heavily indentation-sensitive. Dash items (`-`) must line up perfectly in the exact same vertical column. Do **not** use leading tabs or mismatched whitespace paddings.

```markdown
---
- title: "The OpenCode Revolution"
  description: "An analysis of executing local LLMs on consumer hardware."
  banner: "[https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe](https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe)"
  link: "[https://github.com](https://github.com)"
- title: "Harness Engineering Frameworks"
  description: "Moving beyond fragile prompts into rigid context boundaries."
  banner: "[https://images.unsplash.com/photo-1639762681485-074b7f938ba0](https://images.unsplash.com/photo-1639762681485-074b7f938ba0)"
  link: "[https://github.com](https://github.com)"
---

```

---

## 🚀 Execution & Automation Sequence

Every single time a `git push` is submitted targeting the `main` branch, the internal runner takes care of compilation.

### Initial First-Time Setup Requirements

To allow the repository automation engine to safely deploy code without failing, you must unlock security write clearances:

1. Navigate to your repository dashboard on the **GitHub website**.
2. Click **Settings** (Gear icon) ──► **Actions** ──► **General**.
3. Scroll down to the **Workflow permissions** perimeter block.
4. Select **Read and write permissions**, then click **Save**.

### Tracking and Initial Deployment

Run these commands in your local terminal workspace directory to set up tracking and trigger the workflow for the first time:

```bash
git init
git add .
git commit -m "feat: infrastructure configuration for Claude Aesthetic portfolio"
git branch -M main
git remote add origin [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
git push -u origin main

```

### Activating the Live Website

Once your initial workflow run registers a green checkmark under the **Actions** tab:

1. Click on **Settings** ──► **Pages** in the left-hand navigation sidebar.
2. Under **Build and deployment**, switch the source configuration option to **Deploy from a branch**.
3. Set the specific branch target identifier to **`gh-pages`** and keep the directory at **`/(root)`**.
4. Click **Save**.

Your portfolio is officially live at `https://<YOUR-USERNAME>.github.io/<YOUR-REPO-NAME>/`!

```

***

### How to Apply this to your Repository:
1. Open your local project folder.
2. Open or create a file named exactly `README.md`.
3. Paste the markdown contents provided above inside the file and save.
4. Run the standard update workflow push via your command terminal:
   ```bash
   git add README.md
   git commit -m "docs: implement master system documentation in README"
   git push

```

Your repository home screen is now fully documented, explaining exactly how your automation loops function behind the scenes!