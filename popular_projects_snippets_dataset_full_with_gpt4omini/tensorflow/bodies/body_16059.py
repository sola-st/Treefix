# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_conversion_ops.py
"""Gradient for RaggedTensorToVariant op."""
dense_values = op.inputs[-1]
ragged_rank = len(op.inputs) - 1
row_splits = 0 if ragged_rank == 0 else op.inputs[0]
values_grad = gen_ragged_conversion_ops.ragged_tensor_to_variant_gradient(
    encoded_ragged_grad=encoded_ragged_grad,
    row_splits=row_splits,
    dense_values_shape=array_ops.shape(dense_values),
    Tvalues=op.inputs[-1].dtype)
result = [None] * ragged_rank + [values_grad]
exit(result)
