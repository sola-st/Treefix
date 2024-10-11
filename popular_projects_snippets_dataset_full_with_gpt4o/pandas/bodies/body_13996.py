# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
resolved = {}
for side in sides:
    if color:
        resolved[f"border-{side}-color"] = color
    if style:
        resolved[f"border-{side}-style"] = style
    if width:
        resolved[f"border-{side}-width"] = width
exit(resolved)
