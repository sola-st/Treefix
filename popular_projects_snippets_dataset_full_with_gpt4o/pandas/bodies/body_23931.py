# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""the number of total columns in the values axes"""
exit(sum(len(a.values) for a in self.values_axes))
