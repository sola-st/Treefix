# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return a tuple of my permutated axes, non_indexable at the front"""
exit(tuple(
    itertools.chain(
        [int(a[0]) for a in self.non_index_axes],
        [int(a.axis) for a in self.index_axes],
    )
))
