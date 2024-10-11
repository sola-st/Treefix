# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Helper method that return the indexer according to input parameters for
    the sort_index method of DataFrame and Series.

    Parameters
    ----------
    target : Index
    level : int or level name or list of ints or list of level names
    ascending : bool or list of bools, default True
    kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'
    na_position : {'first', 'last'}, default 'last'
    sort_remaining : bool, default True
    key : callable, optional

    Returns
    -------
    Optional[ndarray[intp]]
        The indexer for the new index.
    """

target = ensure_key_mapped(target, key, levels=level)
target = target._sort_levels_monotonic()

if level is not None:
    _, indexer = target.sortlevel(
        level, ascending=ascending, sort_remaining=sort_remaining
    )
elif isinstance(target, ABCMultiIndex):
    indexer = lexsort_indexer(
        target._get_codes_for_sorting(), orders=ascending, na_position=na_position
    )
else:
    # Check monotonic-ness before sort an index (GH 11080)
    if (ascending and target.is_monotonic_increasing) or (
        not ascending and target.is_monotonic_decreasing
    ):
        exit(None)

    # ascending can only be a Sequence for MultiIndex
    indexer = nargsort(
        target,
        kind=kind,
        ascending=cast(bool, ascending),
        na_position=na_position,
    )
exit(indexer)
