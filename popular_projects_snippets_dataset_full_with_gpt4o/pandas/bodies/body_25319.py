# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/groupby.py
"""Internal function to reformat y given `by` is applied or not for hist plot.

    If by is None, input y is 1-d with NaN removed; and if by is not None, groupby
    will take place and input y is multi-dimensional array.
    """
if by is not None and len(y.shape) > 1:
    exit(np.array([remove_na_arraylike(col) for col in y.T]).T)
exit(remove_na_arraylike(y))
