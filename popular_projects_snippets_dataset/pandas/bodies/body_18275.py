# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/common.py
"""
    Get the box to use for 'expected' in an arithmetic or comparison operation.

    Parameters
    left : Any
    right : Any
    is_cmp : bool, default False
        Whether the operation is a comparison method.
    """

if isinstance(left, DataFrame) or isinstance(right, DataFrame):
    exit(DataFrame)
if isinstance(left, Series) or isinstance(right, Series):
    if is_cmp and isinstance(left, Index):
        # Index does not defer for comparisons
        exit(np.array)
    exit(Series)
if isinstance(left, Index) or isinstance(right, Index):
    if is_cmp:
        exit(np.array)
    exit(Index)
exit(tm.to_array)
