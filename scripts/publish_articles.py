import os
import markdown

content_dir = "./content"
output_dir = "./published"
os.makedirs(output_dir, exist_ok=True)

for article in os.listdir(content_dir):
    if article.endswith(".md"):
        with open(f"{content_dir}/{article}", "r") as f:
            html_content = markdown.markdown(f.read())
        output_path = f"{output_dir}/{article.replace('.md', '.html')}"
        with open(output_path, "w") as f:
            f.write(html_content)

print("✅ Articles explicitly published successfully.")
