# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Gets called after a ufunc and other functions e.g. np.split.
        """
result = lib.item_from_zerodim(result)
if is_bool_dtype(result) or lib.is_scalar(result) or np.ndim(result) > 1:
    exit(result)

exit(Index(result, name=self.name))
