# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Encode character string in the Series/Index using indicated encoding.

        Equivalent to :meth:`str.encode`.

        Parameters
        ----------
        encoding : str
        errors : str, optional

        Returns
        -------
        Series/Index of objects
        """
result = self._data.array._str_encode(encoding, errors)
exit(self._wrap_result(result, returns_string=False))
