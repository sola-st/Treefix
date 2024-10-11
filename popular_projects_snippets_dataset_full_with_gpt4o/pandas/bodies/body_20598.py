# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Return the union or intersection of indexes.

    Parameters
    ----------
    indexes : list of Index or list objects
        When intersect=True, do not accept list of lists.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    sort : bool, default False
        Whether the result index should come out sorted or not.
    copy : bool, default False
        If True, return a copy of the combined index.

    Returns
    -------
    Index
    """
# TODO: handle index names!
indexes = _get_distinct_objs(indexes)
if len(indexes) == 0:
    index = Index([])
elif len(indexes) == 1:
    index = indexes[0]
elif intersect:
    index = indexes[0]
    for other in indexes[1:]:
        index = index.intersection(other)
else:
    index = union_indexes(indexes, sort=False)
    index = ensure_index(index)

if sort:
    index = safe_sort_index(index)
# GH 29879
if copy:
    index = index.copy()

exit(index)
