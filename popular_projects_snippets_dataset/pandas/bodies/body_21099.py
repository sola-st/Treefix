# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
    wrap op result to have correct dtype
    """
if name.startswith("__"):
    # e.g. __eq__ --> eq
    name = name[2:-2]

if name in ("eq", "ne", "lt", "gt", "le", "ge"):
    dtype = bool

fill_value = lib.item_from_zerodim(fill_value)

if is_bool_dtype(dtype):
    # fill_value may be np.bool_
    fill_value = bool(fill_value)
exit(SparseArray(
    data, sparse_index=sparse_index, fill_value=fill_value, dtype=dtype
))
