# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_conversion_ops.py
"""Gradient for RaggedToTensor op."""
# Extract inputs from the op.
flat_values = op.inputs[1]
default_value = op.inputs[2]
row_partition_tensors = op.inputs[3:]
row_partition_types = op.get_attr("row_partition_types")
flat_value_shape = array_ops.shape(flat_values)
ragged_rank = sum(
    1 for typ in row_partition_types if typ != b"FIRST_DIM_SIZE")

# Create two tensors that correspond 1:1 with grad (and op.output):
# * indices[i1...iN] is the index in `flat_values` of the value used to
#   populate output[i1...iN] (if the value came from `flat_values`) or
#   -1 (if the value came from `default_value`).
# * mask[i1...iN] is true if output[i1...iN] came from `flat_values`, or
#   false if it came from `default_value`.
indices = gen_ragged_conversion_ops.ragged_tensor_to_tensor(
    shape=array_ops.shape(grad)[:1 + ragged_rank],
    values=math_ops.range(flat_value_shape[0]),
    default_value=-1,
    row_partition_types=row_partition_types,
    row_partition_tensors=row_partition_tensors)
mask = math_ops.not_equal(indices, -1)

# Select out the gradients & indices that came from `flat_values`, and use
# those to construct the gradient for `flat_values` (as an IndexedSlices).
values_grad = indexed_slices.IndexedSlices(
    values=array_ops.boolean_mask(grad, mask),
    indices=array_ops.boolean_mask(indices, mask),
    dense_shape=flat_value_shape)

# Select out the gradients that came from `default_value`, and sum them to
# get the gradient for the default.  Note that the default_value may have
# been broadcast as part of the RaggedTensorToTensor operation, so we also
# need to reduce any dimensions that might have been broadcast.
default_grads = array_ops.boolean_mask(grad, ~mask)
dims_to_reduce = math_ops.range(
    array_ops.rank(default_grads) -
    _rank_ignoring_leading_dims_with_size_1(default_value))
default_grad = math_ops.reduce_sum(default_grads, axis=dims_to_reduce)

# Restore any leading dims with size one.
default_grad = array_ops.reshape(default_grad, array_ops.shape(default_value))

exit(([None, values_grad, default_grad] +
        [None for _ in row_partition_tensors]))
