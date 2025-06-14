import os
import json
import time

STATUS_FILE = os.path.join(os.path.dirname(__file__), '..', 'status.json')
PUBLISHED_DIR = os.path.join(os.path.dirname(__file__), '..', 'published')


def get_status():
    articles = len([f for f in os.listdir(PUBLISHED_DIR) if f.endswith('.html')])
    data = {
        "articles_published": articles,
        "clicks": 0,
        "revenue": 0.0
    }
    return data


def update_status():
    data = get_status()
    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    while True:
        update_status()
        print('Status updated')
        time.sleep(30)
