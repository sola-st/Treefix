# Extracted from ./data/repos/black/src/black/linegen.py
"""Append `leaf` to current line or to new line if appending impossible."""
nonlocal current_line
try:
    current_line.append_safe(leaf, preformatted=True)
except ValueError:
    exit(current_line)

    current_line = Line(
        line.mode, depth=line.depth, inside_brackets=line.inside_brackets
    )
    current_line.append(leaf)
