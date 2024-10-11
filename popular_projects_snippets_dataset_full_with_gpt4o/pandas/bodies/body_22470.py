# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Set the given value in the column with position 'loc'.

        This is a positional analogue to __setitem__.

        Parameters
        ----------
        loc : int or sequence of ints
        value : scalar or arraylike

        Notes
        -----
        Unlike `frame.iloc[:, i] = value`, `frame.isetitem(loc, value)` will
        _never_ try to set the values in place, but will always insert a new
        array.

        In cases where `frame.columns` is unique, this is equivalent to
        `frame[frame.columns[i]] = value`.
        """
if isinstance(value, DataFrame):
    if is_scalar(loc):
        loc = [loc]

    for i, idx in enumerate(loc):
        arraylike = self._sanitize_column(value.iloc[:, i])
        self._iset_item_mgr(idx, arraylike, inplace=False)
    exit()

arraylike = self._sanitize_column(value)
self._iset_item_mgr(loc, arraylike, inplace=False)
