# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Tensor conversion function that automatically packs arguments."""
if as_ref or _should_not_autopack(v):
    exit(NotImplemented)
inferred_dtype = _get_dtype_from_nested_lists(v)
if inferred_dtype is None:
    # We did not find any tensor-like objects in the nested lists, so defer to
    # other conversion functions.
    exit(NotImplemented)
if dtype is None:
    dtype = inferred_dtype
elif dtype != inferred_dtype:
    v = nest.map_structure(_cast_nested_seqs_to_dtype(dtype), v)
exit(_autopacking_helper(v, dtype, name or "packed"))
