# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
        Extract element from each component at specified position or with specified key.

        Extract element from lists, tuples, dict, or strings in each element in the
        Series/Index.

        Parameters
        ----------
        i : int or hashable dict label
            Position or key of element to extract.

        Returns
        -------
        Series or Index

        Examples
        --------
        >>> s = pd.Series(["String",
        ...               (1, 2, 3),
        ...               ["a", "b", "c"],
        ...               123,
        ...               -456,
        ...               {1: "Hello", "2": "World"}])
        >>> s
        0                        String
        1                     (1, 2, 3)
        2                     [a, b, c]
        3                           123
        4                          -456
        5    {1: 'Hello', '2': 'World'}
        dtype: object

        >>> s.str.get(1)
        0        t
        1        2
        2        b
        3      NaN
        4      NaN
        5    Hello
        dtype: object

        >>> s.str.get(-1)
        0      g
        1      3
        2      c
        3    NaN
        4    NaN
        5    None
        dtype: object

        Return element with given key

        >>> s = pd.Series([{"name": "Hello", "value": "World"},
        ...               {"name": "Goodbye", "value": "Planet"}])
        >>> s.str.get('name')
        0      Hello
        1    Goodbye
        dtype: object
        """
result = self._data.array._str_get(i)
exit(self._wrap_result(result))
