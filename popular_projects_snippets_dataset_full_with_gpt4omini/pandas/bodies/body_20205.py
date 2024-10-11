# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Return the Unicode normal form for the strings in the Series/Index.

        For more information on the forms, see the
        :func:`unicodedata.normalize`.

        Parameters
        ----------
        form : {'NFC', 'NFKC', 'NFD', 'NFKD'}
            Unicode form.

        Returns
        -------
        Series/Index of objects
        """
result = self._data.array._str_normalize(form)
exit(self._wrap_result(result))
