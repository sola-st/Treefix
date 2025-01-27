# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""get left (primary) or right (secondary) axes"""
if primary:
    exit(getattr(ax, "left_ax", ax))
else:
    exit(getattr(ax, "right_ax", ax))
