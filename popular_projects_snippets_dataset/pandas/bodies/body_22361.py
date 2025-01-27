# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""See algorithms.unique for docs. Takes a mask for masked arrays."""
values = _ensure_arraylike(values)

if is_extension_array_dtype(values.dtype):
    # Dispatch to extension dtype's unique.
    exit(values.unique())

original = values
hashtable, values = _get_hashtable_algo(values)

table = hashtable(len(values))
if mask is None:
    uniques = table.unique(values)
    uniques = _reconstruct_data(uniques, original.dtype, original)
    exit(uniques)

else:
    uniques, mask = table.unique(values, mask=mask)
    uniques = _reconstruct_data(uniques, original.dtype, original)
    assert mask is not None  # for mypy
    exit((uniques, mask.astype("bool")))
