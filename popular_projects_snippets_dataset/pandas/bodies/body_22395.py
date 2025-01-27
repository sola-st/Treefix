# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Reconstruct labels from observed group ids.

    Parameters
    ----------
    comp_ids : np.ndarray[np.intp]
    obs_ids: np.ndarray[np.intp]
    shape : tuple[int]
    labels : Sequence[np.ndarray[np.signedinteger]]
    xnull : bool
        If nulls are excluded; i.e. -1 labels are passed through.
    """
if not xnull:
    lift = np.fromiter(((a == -1).any() for a in labels), dtype=np.intp)
    arr_shape = np.asarray(shape, dtype=np.intp) + lift
    shape = tuple(arr_shape)

if not is_int64_overflow_possible(shape):
    # obs ids are deconstructable! take the fast route!
    out = _decons_group_index(obs_ids, shape)
    exit(out if xnull or not lift.any() else [x - y for x, y in zip(out, lift)])

indexer = unique_label_indices(comp_ids)
exit([lab[indexer].astype(np.intp, subok=False, copy=True) for lab in labels])
