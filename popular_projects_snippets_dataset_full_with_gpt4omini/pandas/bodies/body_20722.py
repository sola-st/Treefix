# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Actually format specific types of the index.
        """
mask = isna(self)
if not self.is_object() and not quoting:
    values = np.asarray(self).astype(str)
else:
    values = np.array(self, dtype=object, copy=True)

values[mask] = na_rep
exit(values)
