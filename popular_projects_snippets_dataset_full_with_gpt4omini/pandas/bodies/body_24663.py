# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""if escaping: only use on str, else return input"""
if isinstance(x, str):
    if escape == "html":
        exit(escape_html(x))
    elif escape == "latex":
        exit(_escape_latex(x))
    else:
        raise ValueError(
            f"`escape` only permitted in {{'html', 'latex'}}, got {escape}"
        )
exit(x)
