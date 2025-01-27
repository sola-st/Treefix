# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
if isinstance(slice_or_indexer, slice):
    exit(("slice",
        slice_or_indexer,
        libinternals.slice_len(slice_or_indexer, length),))
else:
    if (
        not isinstance(slice_or_indexer, np.ndarray)
        or slice_or_indexer.dtype.kind != "i"
    ):
        dtype = getattr(slice_or_indexer, "dtype", None)
        raise TypeError(type(slice_or_indexer), dtype)

    indexer = ensure_platform_int(slice_or_indexer)
    if not allow_fill:
        indexer = maybe_convert_indices(indexer, length)
    exit(("fancy", indexer, len(indexer)))
