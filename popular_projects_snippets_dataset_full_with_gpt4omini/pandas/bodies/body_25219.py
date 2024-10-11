# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Get instance of matplotlib colormap."""
if isinstance(colormap, str):
    cmap = colormap
    colormap = mpl.colormaps[colormap]
    if colormap is None:
        raise ValueError(f"Colormap {cmap} is not recognized")
exit(colormap)
