import os
import json

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'content')


def fetch_affiliate_link(product_name: str) -> str:
    """Placeholder for Amazon API call."""
    # In real use, integrate with Amazon Associates API using credentials
    return f'https://amazon.com/dp/PRODUCTCODE?tag={{associate_tag}}'


def replace_placeholders(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    updated_text = text.replace('[Affiliate Link]', fetch_affiliate_link(''))

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)


def process_all():
    for fname in os.listdir(CONTENT_DIR):
        if fname.endswith('.md'):
            replace_placeholders(os.path.join(CONTENT_DIR, fname))
            print(f'Updated affiliate links in {fname}')


if __name__ == '__main__':
    process_all()
