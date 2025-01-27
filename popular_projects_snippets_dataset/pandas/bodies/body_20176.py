# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Determine if each string starts with a match of a regular expression.

        Parameters
        ----------
        pat : str
            Character sequence or regular expression.
        case : bool, default True
            If True, case sensitive.
        flags : int, default 0 (no flags)
            Regex module flags, e.g. re.IGNORECASE.
        na : scalar, optional
            Fill value for missing values. The default depends on dtype of the
            array. For object-dtype, ``numpy.nan`` is used. For ``StringDtype``,
            ``pandas.NA`` is used.

        Returns
        -------
        Series/Index/array of boolean values

        See Also
        --------
        fullmatch : Stricter matching that requires the entire string to match.
        contains : Analogous, but less strict, relying on re.search instead of
            re.match.
        extract : Extract matched groups.
        """
result = self._data.array._str_match(pat, case=case, flags=flags, na=na)
exit(self._wrap_result(result, fill_value=na, returns_string=False))
