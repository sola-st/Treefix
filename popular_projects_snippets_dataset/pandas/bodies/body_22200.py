# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
orig_vals = values
if isinstance(values, BaseMaskedArray):
    mask = values._mask
    result_mask = np.zeros((ngroups, nqs), dtype=np.bool_)
else:
    mask = isna(values)
    result_mask = None

vals, inference = pre_processor(values)

ncols = 1
if vals.ndim == 2:
    ncols = vals.shape[0]
    shaped_labels = np.broadcast_to(
        labels_for_lexsort, (ncols, len(labels_for_lexsort))
    )
else:
    shaped_labels = labels_for_lexsort

out = np.empty((ncols, ngroups, nqs), dtype=np.float64)

# Get an index of values sorted by values and then labels
order = (vals, shaped_labels)
sort_arr = np.lexsort(order).astype(np.intp, copy=False)

if vals.ndim == 1:
    # Ea is always 1d
    func(
        out[0],
        values=vals,
        mask=mask,
        sort_indexer=sort_arr,
        result_mask=result_mask,
    )
else:
    for i in range(ncols):
        func(out[i], values=vals[i], mask=mask[i], sort_indexer=sort_arr[i])

if vals.ndim == 1:
    out = out.ravel("K")
    if result_mask is not None:
        result_mask = result_mask.ravel("K")
else:
    out = out.reshape(ncols, ngroups * nqs)
exit(post_processor(out, inference, result_mask, orig_vals))
