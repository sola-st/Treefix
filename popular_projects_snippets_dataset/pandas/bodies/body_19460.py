# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Try to infer an Index from the passed data, raise ValueError on failure.
    """
index: Index
if len(data) == 0:
    exit(default_index(0))

raw_lengths = []
indexes: list[list[Hashable] | Index] = []

have_raw_arrays = False
have_series = False
have_dicts = False

for val in data:
    if isinstance(val, ABCSeries):
        have_series = True
        indexes.append(val.index)
    elif isinstance(val, dict):
        have_dicts = True
        indexes.append(list(val.keys()))
    elif is_list_like(val) and getattr(val, "ndim", 1) == 1:
        have_raw_arrays = True
        raw_lengths.append(len(val))
    elif isinstance(val, np.ndarray) and val.ndim > 1:
        raise ValueError("Per-column arrays must each be 1-dimensional")

if not indexes and not raw_lengths:
    raise ValueError("If using all scalar values, you must pass an index")

if have_series:
    index = union_indexes(indexes)
elif have_dicts:
    index = union_indexes(indexes, sort=False)

if have_raw_arrays:
    lengths = list(set(raw_lengths))
    if len(lengths) > 1:
        raise ValueError("All arrays must be of the same length")

    if have_dicts:
        raise ValueError(
            "Mixing dicts with non-Series may lead to ambiguous ordering."
        )

    if have_series:
        if lengths[0] != len(index):
            msg = (
                f"array length {lengths[0]} does not match index "
                f"length {len(index)}"
            )
            raise ValueError(msg)
    else:
        index = default_index(lengths[0])

exit(ensure_index(index))
