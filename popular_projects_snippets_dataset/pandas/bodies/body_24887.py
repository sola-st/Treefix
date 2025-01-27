# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
if not text_only:
    dark = relative_luminance(rgba) < text_color_threshold
    text_color = "#f1f1f1" if dark else "#000000"
    exit((
        f"background-color: {_matplotlib.colors.rgb2hex(rgba)};"
        + f"color: {text_color};"
    ))
else:
    exit(f"color: {_matplotlib.colors.rgb2hex(rgba)};")
