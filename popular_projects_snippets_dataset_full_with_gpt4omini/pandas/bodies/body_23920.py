# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the axis for c"""
for a in self.axes:
    if c == a.name:
        exit(a)
exit(None)
