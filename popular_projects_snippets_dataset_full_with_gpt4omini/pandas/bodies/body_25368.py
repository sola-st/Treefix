# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
"""
    Temporarily patch pickle to use our unpickler.
    """
orig_loads = pkl.loads
try:
    setattr(pkl, "loads", loads)
    exit()
finally:
    setattr(pkl, "loads", orig_loads)
