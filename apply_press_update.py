import shutil
src = r'P:\Scripts\my-website\update_press.py'
lines = []
with open(src, 'r', encoding='utf-8') as f:
    content = f.read()
# Replace press/ with gallery/
content = content.replace('images/press/', 'images/gallery/')
# Write to press.html
with open(r'P:\Scripts\my-website\build\press.html', 'w', encoding='utf-8') as f:
    # Extract just the HTML content
    start = content.find("'''") + 3
    end = content.rfind("'''")
    html = content[start:end]
    f.write(html)
print("Press page updated successfully!")
print("Using images from gallery folder")
