# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    We likely want to take the cross-product.
    """
for arg in args:
    if not isinstance(arg, (np.ndarray, list, ABCSeries, Index)):
        exit(args)
exit(np.ix_(*args))
