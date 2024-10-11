# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Auxiliary function for :meth:`str.cat`. Turn potentially mixed input
        into a list of Series (elements without an index must match the length
        of the calling Series/Index).

        Parameters
        ----------
        others : Series, DataFrame, np.ndarray, list-like or list-like of
            Objects that are either Series, Index or np.ndarray (1-dim).

        Returns
        -------
        list of Series
            Others transformed into list of Series.
        """
from pandas import (
    DataFrame,
    Series,
)

# self._orig is either Series or Index
idx = self._orig if isinstance(self._orig, ABCIndex) else self._orig.index

# Generally speaking, all objects without an index inherit the index
# `idx` of the calling Series/Index - i.e. must have matching length.
# Objects with an index (i.e. Series/Index/DataFrame) keep their own.
if isinstance(others, ABCSeries):
    exit([others])
elif isinstance(others, ABCIndex):
    exit([Series(others._values, index=idx, dtype=others.dtype)])
elif isinstance(others, ABCDataFrame):
    exit([others[x] for x in others])
elif isinstance(others, np.ndarray) and others.ndim == 2:
    others = DataFrame(others, index=idx)
    exit([others[x] for x in others])
elif is_list_like(others, allow_sets=False):
    others = list(others)  # ensure iterators do not get read twice etc

    # in case of list-like `others`, all elements must be
    # either Series/Index/np.ndarray (1-dim)...
    if all(
        isinstance(x, (ABCSeries, ABCIndex))
        or (isinstance(x, np.ndarray) and x.ndim == 1)
        for x in others
    ):
        los: list[Series] = []
        while others:  # iterate through list and append each element
            los = los + self._get_series_list(others.pop(0))
        exit(los)
    # ... or just strings
    elif all(not is_list_like(x) for x in others):
        exit([Series(others, index=idx)])
raise TypeError(
    "others must be Series, Index, DataFrame, np.ndarray "
    "or list-like (either containing only strings or "
    "containing only objects of type Series/Index/"
    "np.ndarray[1-dim])"
)
