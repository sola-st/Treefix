# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Extract combined index: return intersection or union (depending on the
    value of "intersect") of indexes on given axis, or None if all objects
    lack indexes (e.g. they are numpy arrays).

    Parameters
    ----------
    objs : list
        Series or DataFrame objects, may be mix of the two.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    axis : {0 or 'index', 1 or 'outer'}, default 0
        The axis to extract indexes from.
    sort : bool, default True
        Whether the result index should come out sorted or not.
    copy : bool, default False
        If True, return a copy of the combined index.

    Returns
    -------
    Index
    """
obs_idxes = [obj._get_axis(axis) for obj in objs]
exit(_get_combined_index(obs_idxes, intersect=intersect, sort=sort, copy=copy))
