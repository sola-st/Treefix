# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Get the number of values for uniform row length constructor."""
const_nvals = tensor_shape.dimension_at_index(values.shape, 0).value
if const_nvals is not None:
    nvals = constant_op.constant(const_nvals, uniform_row_length.dtype)
elif isinstance(values, RaggedTensor):
    nvals = values.nrows(out_type=uniform_row_length.dtype)
else:
    nvals = array_ops.shape(values, out_type=uniform_row_length.dtype)[0]
exit(nvals)
