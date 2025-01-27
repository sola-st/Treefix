# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Map all characters in the string through the given mapping table.

        Equivalent to standard :meth:`str.translate`.

        Parameters
        ----------
        table : dict
            Table is a mapping of Unicode ordinals to Unicode ordinals, strings, or
            None. Unmapped characters are left untouched.
            Characters mapped to None are deleted. :meth:`str.maketrans` is a
            helper function for making translation tables.

        Returns
        -------
        Series or Index
        """
result = self._data.array._str_translate(table)
exit(self._wrap_result(result))
