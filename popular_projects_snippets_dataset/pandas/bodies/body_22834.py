# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
indexer = ensure_platform_int(indexer)
_take_nd_object(
    arr, indexer, out, axis=axis, fill_value=fill_value, mask_info=mask_info
)
