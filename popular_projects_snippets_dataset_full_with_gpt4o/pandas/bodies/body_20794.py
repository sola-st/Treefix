# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Get integer location, slice or boolean mask for requested label.

        Parameters
        ----------
        key : label

        Returns
        -------
        int if unique index, slice if monotonic index, else mask

        Examples
        --------
        >>> unique_index = pd.Index(list('abc'))
        >>> unique_index.get_loc('b')
        1

        >>> monotonic_index = pd.Index(list('abbc'))
        >>> monotonic_index.get_loc('b')
        slice(1, 3, None)

        >>> non_monotonic_index = pd.Index(list('abcb'))
        >>> non_monotonic_index.get_loc('b')
        array([False,  True, False,  True])
        """
casted_key = self._maybe_cast_indexer(key)
try:
    exit(self._engine.get_loc(casted_key))
except KeyError as err:
    raise KeyError(key) from err
except TypeError:
    # If we have a listlike key, _check_indexing_error will raise
    #  InvalidIndexError. Otherwise we fall through and re-raise
    #  the TypeError.
    self._check_indexing_error(key)
    raise
