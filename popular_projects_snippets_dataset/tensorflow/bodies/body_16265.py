# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Gradient for RaggedTensorToSparse."""
op_inputs_nested_row_splits = op.inputs[:-1]
op_inputs_flat_values = op.inputs[-1]

# No gradient for the RaggedTensor's nested_row_splits.
nested_row_splits_gradient = [None] * len(op_inputs_nested_row_splits)

# Gradient for the RaggedTensor's flat_values is formed by reshaping
# the gradient for the SparseTensor's values.
flat_values_shape = array_ops.shape(op_inputs_flat_values)
flat_values_gradient = array_ops.reshape(sparse_values_grad,
                                         flat_values_shape)

exit(nested_row_splits_gradient + [flat_values_gradient])
