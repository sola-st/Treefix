# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Called from get_indexer or get_indexer_non_unique when the target
        is of a non-comparable dtype.

        For get_indexer lookups with method=None, get_indexer is an _equality_
        check, so non-comparable dtypes mean we will always have no matches.

        For get_indexer lookups with a method, get_indexer is an _inequality_
        check, so non-comparable dtypes mean we will always raise TypeError.

        Parameters
        ----------
        target : Index
        method : str or None
        unique : bool, default True
            * True if called from get_indexer.
            * False if called from get_indexer_non_unique.

        Raises
        ------
        TypeError
            If doing an inequality check, i.e. method is not None.
        """
if method is not None:
    other = unpack_nested_dtype(target)
    raise TypeError(f"Cannot compare dtypes {self.dtype} and {other.dtype}")

no_matches = -1 * np.ones(target.shape, dtype=np.intp)
if unique:
    # This is for get_indexer
    exit(no_matches)
else:
    # This is for get_indexer_non_unique
    missing = np.arange(len(target), dtype=np.intp)
    exit((no_matches, missing))
