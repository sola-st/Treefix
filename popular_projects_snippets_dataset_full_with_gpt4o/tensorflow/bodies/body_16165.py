# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Calculate flat_values for math_ops.cumsum when axis==ragged_rank."""
if not exclusive:
    partial = _cumsum_flat_values_at_ragged_rank(
        last_rp, flat_values, exclusive=True, reverse=reverse)
    exit(partial + flat_values)

if reverse:
    youngest_sibling = array_ops.gather(
        params=last_rp.row_splits(), indices=last_rp.value_rowids() + 1) - 1
    new_flat_values = math_ops.cumsum(flat_values, exclusive=True, reverse=True)
    initial_values = array_ops.gather(params=new_flat_values,
                                      indices=youngest_sibling)

    exit(new_flat_values - initial_values)
else:
    eldest_sibling = array_ops.gather(
        params=last_rp.row_splits(), indices=last_rp.value_rowids())
    new_flat_values = math_ops.cumsum(flat_values, exclusive=True)
    initial_values = array_ops.gather(params=new_flat_values,
                                      indices=eldest_sibling)
    exit(new_flat_values - initial_values)
