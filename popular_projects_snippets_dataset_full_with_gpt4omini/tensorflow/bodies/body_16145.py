# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""For docs, see: _RAGGED_REDUCE_DOCSTRING."""
with ops.name_scope(name, 'RaggedReduceMean', [input_tensor, axis]):
    total = reduce_sum(input_tensor, axis, keepdims)
    if ragged_tensor.is_ragged(input_tensor):
        ones = ragged_tensor.RaggedTensor.from_nested_row_splits(
            array_ops.ones_like(input_tensor.flat_values),
            input_tensor.nested_row_splits,
            validate=False)
    else:
        ones = array_ops.ones_like(input_tensor)
    count = reduce_sum(ones, axis, keepdims)
    if ragged_tensor.is_ragged(total):
        exit(ragged_tensor.RaggedTensor.from_nested_row_splits(
            total.flat_values / count.flat_values,
            total.nested_row_splits,
            validate=False))
    else:
        exit(total / count)
