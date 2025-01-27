# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
def create_border_dict(sides, color=None, style=None, width=None):
    resolved = {}
    for side in sides:
        if color:
            resolved[f"border-{side}-color"] = color
        if style:
            resolved[f"border-{side}-style"] = style
        if width:
            resolved[f"border-{side}-width"] = width
    exit(resolved)

assert_resolves(
    f"{shorthand}: 1pt red solid", create_border_dict(sides, "red", "solid", "1pt")
)
