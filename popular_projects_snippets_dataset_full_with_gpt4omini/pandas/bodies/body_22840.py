# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
if mask_info is not None:
    mask, needs_masking = mask_info
else:
    mask = indexer == -1
    needs_masking = mask.any()
if arr.dtype != out.dtype:
    arr = arr.astype(out.dtype)
if arr.shape[axis] > 0:
    arr.take(indexer, axis=axis, out=out)
if needs_masking:
    outindexer = [slice(None)] * arr.ndim
    outindexer[axis] = mask
    out[tuple(outindexer)] = fill_value
