import os
import re

raw_text = input('Input text to parse: ')

tokens = re.split(r'(\[Key\.[^\]]+\])', raw_text)

result = []

for token in tokens:
    if token == '[Key.space]':
        result.append(' ')
    elif token == '[Key.enter]':
        result.append('\n')
    elif token == '[Key.backspace]':
        if result:
            result.pop()
    elif token.startswith('[Key.'):
        continue
    else:
        result.append(token)

parsed_text = ''.join(result)

folder_name = "parsed_keylogs"


i = 1
while True:
    filename = f"parsed_keylog_{i}.txt"
    filepath = os.path.join(folder_name, filename)
    
    if not os.path.exists(filepath):
        break
    i += 1

# Write file
with open(filepath, "w", encoding="utf-8") as f:
    f.write(parsed_text)

print(f"Saved to: {filepath}")