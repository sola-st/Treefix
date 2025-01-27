# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        Filter elements from groups that don't satisfy a criterion.

        Elements from groups are filtered if they do not satisfy the
        boolean criterion specified by func.

        Parameters
        ----------
        func : function
            Criterion to apply to each group. Should return True or False.
        dropna : bool
            Drop groups that do not pass the filter. True by default; if False,
            groups that evaluate False are filled with NaNs.

        Returns
        -------
        Series

        Notes
        -----
        Functions that mutate the passed object can produce unexpected
        behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
        for more details.

        Examples
        --------
        >>> df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
        ...                           'foo', 'bar'],
        ...                    'B' : [1, 2, 3, 4, 5, 6],
        ...                    'C' : [2.0, 5., 8., 1., 2., 9.]})
        >>> grouped = df.groupby('A')
        >>> df.groupby('A').B.filter(lambda x: x.mean() > 3.)
        1    2
        3    4
        5    6
        Name: B, dtype: int64
        """
if isinstance(func, str):
    wrapper = lambda x: getattr(x, func)(*args, **kwargs)
else:
    wrapper = lambda x: func(x, *args, **kwargs)

# Interpret np.nan as False.
def true_and_notna(x) -> bool:
    b = wrapper(x)
    exit(b and notna(b))

try:
    indices = [
        self._get_index(name) for name, group in self if true_and_notna(group)
    ]
except (ValueError, TypeError) as err:
    raise TypeError("the filter must return a boolean result") from err

filtered = self._apply_filter(indices, dropna)
exit(filtered)
