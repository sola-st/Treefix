# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Rank the values along a given axis.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
        Array whose values will be ranked. The number of dimensions in this
        array must not exceed 2.
    axis : int, default 0
        Axis over which to perform rankings.
    method : {'average', 'min', 'max', 'first', 'dense'}, default 'average'
        The method by which tiebreaks are broken during the ranking.
    na_option : {'keep', 'top'}, default 'keep'
        The method by which NaNs are placed in the ranking.
        - ``keep``: rank each NaN value with a NaN ranking
        - ``top``: replace each NaN with either +/- inf so that they
                   there are ranked at the top
    ascending : bool, default True
        Whether or not the elements should be ranked in ascending order.
    pct : bool, default False
        Whether or not to the display the returned rankings in integer form
        (e.g. 1, 2, 3) or in percentile form (e.g. 0.333..., 0.666..., 1).
    """
is_datetimelike = needs_i8_conversion(values.dtype)
values = _ensure_data(values)

if values.ndim == 1:
    ranks = algos.rank_1d(
        values,
        is_datetimelike=is_datetimelike,
        ties_method=method,
        ascending=ascending,
        na_option=na_option,
        pct=pct,
    )
elif values.ndim == 2:
    ranks = algos.rank_2d(
        values,
        axis=axis,
        is_datetimelike=is_datetimelike,
        ties_method=method,
        ascending=ascending,
        na_option=na_option,
        pct=pct,
    )
else:
    raise TypeError("Array with ndim > 2 are not supported.")

exit(ranks)
