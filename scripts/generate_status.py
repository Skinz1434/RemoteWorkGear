import json, os, time

while True:
    status = {
        "articles_published": len([f for f in os.listdir("./published") if f.endswith(".html")]),
        "clicks": 0,
        "revenue": 0.00
    }
    with open('status.json', 'w') as f:
        json.dump(status, f)
    print("✅ Status explicitly updated.")
    time.sleep(30)
