# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/scipy_sparse.py
"""
    For a MultiIndexed sparse Series `ss`, return `ax_coords` and `ax_labels`,
    where `ax_coords` are the coordinates along one of the two axes of the
    destination sparse matrix, and `ax_labels` are the labels from `ss`' Index
    which correspond to these coordinates.

    Parameters
    ----------
    ss : Series
    levels : tuple/list
    valid_ilocs : numpy.ndarray
        Array of integer positions of valid values for the sparse matrix in ss.
    sort_labels : bool, default False
        Sort the axis labels before forming the sparse matrix. When `levels`
        refers to a single level, set to True for a faster execution.

    Returns
    -------
    ax_coords : numpy.ndarray (axis coordinates)
    ax_labels : list (axis labels)
    """
# Since the labels are sorted in `Index.levels`, when we wish to sort and
# there is only one level of the MultiIndex for this axis, the desired
# output can be obtained in the following simpler, more efficient way.
if sort_labels and len(levels) == 1:
    ax_coords = ss.index.codes[levels[0]][valid_ilocs]
    ax_labels = ss.index.levels[levels[0]]

else:
    levels_values = lib.fast_zip(
        [ss.index.get_level_values(lvl).values for lvl in levels]
    )
    codes, ax_labels = factorize(levels_values, sort=sort_labels)
    ax_coords = codes[valid_ilocs]

ax_labels = ax_labels.tolist()
exit((ax_coords, ax_labels))
