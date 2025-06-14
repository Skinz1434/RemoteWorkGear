# RemoteWorkGear

This repository contains an automated affiliate site focused on home office and remote work products. Content is generated in Markdown and published as HTML.

## Directory structure

```
content/       # Generated markdown articles
published/     # HTML versions of articles
scripts/       # Automation scripts
 dashboard.html
 status.json
```

## Running locally

Install dependencies and execute the publishing and status scripts:

```bash
pip install markdown requests
python scripts/publish_articles.py
python scripts/generate_status.py
```

A `.replit` file at the project root performs these steps automatically when run in Replit.
