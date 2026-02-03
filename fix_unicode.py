import re

with open('create_map_poster.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace Unicode symbols only in print statements
modified_lines = []
for line in lines:
    # Replace Unicode symbols with ASCII equivalents
    line = line.replace('\u2713', '[+]')  # ✓
    line = line.replace('\u26a0', '[!]')  # ⚠
    line = line.replace('\u2717', '[X]')  # ✗
    line = line.replace('\u25cf', '*')    # ●
    modified_lines.append(line)

with open('create_map_poster.py', 'w', encoding='utf-8') as f:
    f.writelines(modified_lines)

print('Successfully replaced Unicode symbols in create_map_poster.py')
