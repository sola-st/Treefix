# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Gradient for RaggedGather op."""
param_nested_splits = op.inputs[:-2]
param_inner_values = op.inputs[-2]
indices = op.inputs[-1]
grad_inner_values = grads[-1]

# For each row in `params`, find the range of values in `params.inner_values`
# that is covered by that row.  In particular, the values in row `i` are
# `param_inner_values[combined_splits[i]:combined_splits[i+1]`.
combined_splits = param_nested_splits[0]
for row_splits in param_nested_splits[1:]:
    combined_splits = array_ops.gather(row_splits, combined_splits)

# The outer dimensions of `indices` correspond 1:1 with the outer dimensions
# of `ragged_grad` that are encoded by `grad_nested_splits`.  Thus, the
# flattened `indices` correspond 1:1 with `grad_inner_values`.
flat_indices = array_ops.reshape(indices, [-1])

# Build an IndexedSlices where the values are taken from `flat_grad`.
grad_indices = ragged_math_ops.range(
    array_ops.gather(combined_splits, flat_indices),
    array_ops.gather(combined_splits[1:], flat_indices)).values

param_inner_values_grad = indexed_slices.IndexedSlices(
    values=grad_inner_values, indices=grad_indices,
    dense_shape=array_ops.shape(param_inner_values))
exit([None for _ in param_nested_splits] + [param_inner_values_grad, None])
