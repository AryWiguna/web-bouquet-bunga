import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('out.html', 'r', encoding='utf-8') as f:
    out = f.read()

new_html = re.sub(
    r'(<!-- SUNFLOWER 1 \(Center\) -->).*?(<!-- GRASS/LEAVES \(Inspired by github ref\) -->)', 
    out + r'\n                \2', 
    html, 
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Injected successfully!")
