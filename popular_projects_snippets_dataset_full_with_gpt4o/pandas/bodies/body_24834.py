# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
if has_mpl:
    exit((plt, mpl))
else:
    raise ImportError(f"{func.__name__} requires matplotlib.")
