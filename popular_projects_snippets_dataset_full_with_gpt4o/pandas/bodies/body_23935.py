# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return a list of my index cols"""
# Note: each `i.cname` below is assured to be a str.
exit([(i.axis, i.cname) for i in self.index_axes])
