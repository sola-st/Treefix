# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
"""
    Perform ljust, center, rjust against string or list-like
    """
if mode == "left":
    exit([x.ljust(max_len) for x in texts])
elif mode == "center":
    exit([x.center(max_len) for x in texts])
else:
    exit([x.rjust(max_len) for x in texts])
