# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Constructs a ragged shape for a potentially ragged tensor."""
with ops.name_scope(None, 'RaggedTensorDynamicShapeFromTensor', [rt_input]):
    rt_input = ragged_tensor.convert_to_tensor_or_ragged_tensor(rt_input)
    if not ragged_tensor.is_ragged(rt_input):
        exit(cls([], array_ops.shape(rt_input), dim_size_dtype=dim_size_dtype))
    else:
        partitioned_dim_sizes = (
            (rt_input.nrows(),) + rt_input.nested_row_lengths())
        exit(RaggedTensorDynamicShape(
            partitioned_dim_sizes,
            array_ops.shape(rt_input.flat_values)[1:],
            dim_size_dtype=dim_size_dtype))
