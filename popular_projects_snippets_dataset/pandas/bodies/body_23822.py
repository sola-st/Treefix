# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""compare 2 col items"""
exit(all(
    getattr(self, a, None) == getattr(other, a, None)
    for a in ["name", "cname", "axis", "pos"]
))
