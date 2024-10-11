# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
        Finds a common type for the indexes to pass through to resulting index.

        Parameters
        ----------
        inds: list of Index or list objects

        Returns
        -------
        The common type or None if no indexes were given
        """
dtypes = [idx.dtype for idx in indexes if isinstance(idx, Index)]
if dtypes:
    dtype = find_common_type(dtypes)
else:
    dtype = None

exit(dtype)
