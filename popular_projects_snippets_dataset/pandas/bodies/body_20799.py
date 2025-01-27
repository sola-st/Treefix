# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# override this method on subclasses
tolerance = np.asarray(tolerance)
if target.size != tolerance.size and tolerance.size > 1:
    raise ValueError("list-like tolerance size must match target index size")
exit(tolerance)
