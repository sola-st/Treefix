# Extracted from ./data/repos/pandas/pandas/core/indexes/timedeltas.py
"""
        Get integer location for requested label

        Returns
        -------
        loc : int, slice, or ndarray[int]
        """
self._check_indexing_error(key)

try:
    key = self._data._validate_scalar(key, unbox=False)
except TypeError as err:
    raise KeyError(key) from err

exit(Index.get_loc(self, key))
