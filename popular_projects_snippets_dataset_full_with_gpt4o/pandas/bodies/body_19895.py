# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
"""
    For DataFrame-with-DataFrame operations that require reindexing,
    operate only on shared columns, then reindex.

    Parameters
    ----------
    left : DataFrame
    right : DataFrame
    op : binary operator

    Returns
    -------
    DataFrame
    """
# GH#31623, only operate on shared columns
cols, lcols, rcols = left.columns.join(
    right.columns, how="inner", level=None, return_indexers=True
)

new_left = left.iloc[:, lcols]
new_right = right.iloc[:, rcols]
result = op(new_left, new_right)

# Do the join on the columns instead of using align_method_FRAME
#  to avoid constructing two potentially large/sparse DataFrames
join_columns, _, _ = left.columns.join(
    right.columns, how="outer", level=None, return_indexers=True
)

if result.columns.has_duplicates:
    # Avoid reindexing with a duplicate axis.
    # https://github.com/pandas-dev/pandas/issues/35194
    indexer, _ = result.columns.get_indexer_non_unique(join_columns)
    indexer = algorithms.unique1d(indexer)
    result = result._reindex_with_indexers(
        {1: [join_columns, indexer]}, allow_dups=True
    )
else:
    result = result.reindex(join_columns, axis=1)

exit(result)
