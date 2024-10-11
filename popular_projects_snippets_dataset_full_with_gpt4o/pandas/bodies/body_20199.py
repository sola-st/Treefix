# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Test if the end of each string element matches a pattern.

        Equivalent to :meth:`str.endswith`.

        Parameters
        ----------
        pat : str or tuple[str, ...]
            Character sequence or tuple of strings. Regular expressions are not
            accepted.
        na : object, default NaN
            Object shown if element tested is not a string. The default depends
            on dtype of the array. For object-dtype, ``numpy.nan`` is used.
            For ``StringDtype``, ``pandas.NA`` is used.

        Returns
        -------
        Series or Index of bool
            A Series of booleans indicating whether the given pattern matches
            the end of each string element.

        See Also
        --------
        str.endswith : Python standard library string method.
        Series.str.startswith : Same as endswith, but tests the start of string.
        Series.str.contains : Tests if string element contains a pattern.

        Examples
        --------
        >>> s = pd.Series(['bat', 'bear', 'caT', np.nan])
        >>> s
        0     bat
        1    bear
        2     caT
        3     NaN
        dtype: object

        >>> s.str.endswith('t')
        0     True
        1    False
        2    False
        3      NaN
        dtype: object

        >>> s.str.endswith(('t', 'T'))
        0     True
        1    False
        2     True
        3      NaN
        dtype: object

        Specifying `na` to be `False` instead of `NaN`.

        >>> s.str.endswith('t', na=False)
        0     True
        1    False
        2    False
        3    False
        dtype: bool
        """
if not isinstance(pat, (str, tuple)):
    msg = f"expected a string or tuple, not {type(pat).__name__}"
    raise TypeError(msg)
result = self._data.array._str_endswith(pat, na=na)
exit(self._wrap_result(result, returns_string=False))
