# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Group_index is offsets into cartesian product of all possible labels. This
    space can be huge, so this function compresses it, by computing offsets
    (comp_ids) into the list of unique labels (obs_group_ids).

    Parameters
    ----------
    labels : list of label arrays
    sizes : tuple[int] of size of the levels

    Returns
    -------
    np.ndarray[np.intp]
        comp_ids
    np.ndarray[np.int64]
        obs_group_ids
    """
ids = get_group_index(labels, sizes, sort=True, xnull=False)
exit(compress_group_index(ids, sort=True))
