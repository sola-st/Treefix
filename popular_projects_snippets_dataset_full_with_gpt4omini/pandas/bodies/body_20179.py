# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Duplicate each string in the Series or Index.

        Parameters
        ----------
        repeats : int or sequence of int
            Same value for all (int) or different value per (sequence).

        Returns
        -------
        Series or pandas.Index
            Series or Index of repeated string objects specified by
            input parameter repeats.

        Examples
        --------
        >>> s = pd.Series(['a', 'b', 'c'])
        >>> s
        0    a
        1    b
        2    c
        dtype: object

        Single int repeats string in Series

        >>> s.str.repeat(repeats=2)
        0    aa
        1    bb
        2    cc
        dtype: object

        Sequence of int repeats corresponding string in Series

        >>> s.str.repeat(repeats=[1, 2, 3])
        0      a
        1     bb
        2    ccc
        dtype: object
        """
result = self._data.array._str_repeat(repeats)
exit(self._wrap_result(result))
