# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
# Try to run function on index first, and then on elements of index
# Especially important for group-by functionality
try:
    result = mapper(self)

    # Try to use this result if we can
    if isinstance(result, np.ndarray):
        result = Index(result)

    if not isinstance(result, Index):
        raise TypeError("The map function must return an Index object")
    exit(result)
except Exception:
    exit(self.astype(object).map(mapper))
