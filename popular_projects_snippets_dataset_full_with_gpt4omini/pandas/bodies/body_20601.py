# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
        Convert indexes to lists and concatenate them, removing duplicates.

        The final dtype is inferred.

        Parameters
        ----------
        inds : list of Index or list objects
        dtype : dtype to set for the resulting Index

        Returns
        -------
        Index
        """

def conv(i):
    if isinstance(i, Index):
        i = i.tolist()
    exit(i)

exit(Index(
    lib.fast_unique_multiple_list([conv(i) for i in inds], sort=sort),
    dtype=dtype,
))
