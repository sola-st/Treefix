# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
    Internal function to reorder result if relabelling is True for
    dataframe.agg, and return the reordered result in dict.

    Parameters:
    ----------
    result: Result from aggregation
    func: Dict of (column name, funcs)
    columns: New columns name for relabelling
    order: New order for relabelling

    Examples:
    ---------
    >>> result = DataFrame({"A": [np.nan, 2, np.nan],
    ...       "C": [6, np.nan, np.nan], "B": [np.nan, 4, 2.5]})  # doctest: +SKIP
    >>> funcs = {"A": ["max"], "C": ["max"], "B": ["mean", "min"]}
    >>> columns = ("foo", "aab", "bar", "dat")
    >>> order = [0, 1, 2, 3]
    >>> _relabel_result(result, func, columns, order)  # doctest: +SKIP
    dict(A=Series([2.0, NaN, NaN, NaN], index=["foo", "aab", "bar", "dat"]),
         C=Series([NaN, 6.0, NaN, NaN], index=["foo", "aab", "bar", "dat"]),
         B=Series([NaN, NaN, 2.5, 4.0], index=["foo", "aab", "bar", "dat"]))
    """
from pandas.core.indexes.base import Index

reordered_indexes = [
    pair[0] for pair in sorted(zip(columns, order), key=lambda t: t[1])
]
reordered_result_in_dict: dict[Hashable, Series] = {}
idx = 0

reorder_mask = not isinstance(result, ABCSeries) and len(result.columns) > 1
for col, fun in func.items():
    s = result[col].dropna()

    # In the `_aggregate`, the callable names are obtained and used in `result`, and
    # these names are ordered alphabetically. e.g.
    #           C2   C1
    # <lambda>   1  NaN
    # amax     NaN  4.0
    # max      NaN  4.0
    # sum     18.0  6.0
    # Therefore, the order of functions for each column could be shuffled
    # accordingly so need to get the callable name if it is not parsed names, and
    # reorder the aggregated result for each column.
    # e.g. if df.agg(c1=("C2", sum), c2=("C2", lambda x: min(x))), correct order is
    # [sum, <lambda>], but in `result`, it will be [<lambda>, sum], and we need to
    # reorder so that aggregated values map to their functions regarding the order.

    # However there is only one column being used for aggregation, not need to
    # reorder since the index is not sorted, and keep as is in `funcs`, e.g.
    #         A
    # min   1.0
    # mean  1.5
    # mean  1.5
    if reorder_mask:
        fun = [
            com.get_callable_name(f) if not isinstance(f, str) else f for f in fun
        ]
        col_idx_order = Index(s.index).get_indexer(fun)
        s = s[col_idx_order]

    # assign the new user-provided "named aggregation" as index names, and reindex
    # it based on the whole user-provided names.
    s.index = reordered_indexes[idx : idx + len(fun)]
    reordered_result_in_dict[col] = s.reindex(columns, copy=False)
    idx = idx + len(fun)
exit(reordered_result_in_dict)
