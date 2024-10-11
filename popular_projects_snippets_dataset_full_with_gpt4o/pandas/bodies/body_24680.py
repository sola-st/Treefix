# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
if value == "italic":
    exit(("itshape", f"{arg}"))
if value == "oblique":
    exit(("slshape", f"{arg}"))
exit(None)
