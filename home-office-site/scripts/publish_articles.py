import os
from markdown import markdown

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'content')
PUBLISHED_DIR = os.path.join(os.path.dirname(__file__), '..', 'published')


def convert_markdown_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    html = markdown(text)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)


def publish_all():
    os.makedirs(PUBLISHED_DIR, exist_ok=True)
    for fname in os.listdir(CONTENT_DIR):
        if fname.endswith('.md'):
            md_file = os.path.join(CONTENT_DIR, fname)
            html_file = os.path.splitext(fname)[0] + '.html'
            html_path = os.path.join(PUBLISHED_DIR, html_file)
            convert_markdown_to_html(md_file, html_path)
            print(f'Published {html_file}')


if __name__ == '__main__':
    publish_all()
