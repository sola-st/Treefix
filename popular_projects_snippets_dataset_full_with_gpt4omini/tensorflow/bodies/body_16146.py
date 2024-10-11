# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""For docs, see: _RAGGED_REDUCE_DOCSTRING."""
with ops.name_scope(name, 'RaggedReduceVariance', [input_tensor, axis]):
    input_tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        input_tensor, name='input_tensor')
    if input_tensor.dtype.is_complex:
        raise ValueError(
            'reduce_variance is not supported for RaggedTensors with complex dtypes.'
        )
    square_of_input = math_ops.square(input_tensor)
    mean_of_square = reduce_mean(square_of_input, axis=axis, keepdims=keepdims)
    mean = reduce_mean(input_tensor, axis=axis, keepdims=keepdims)
    square_of_mean = math_ops.square(mean)
    # Note: the above method of computing variance is not numerically stable,
    # and can result in negative variances.  Here we clip to >= 0.
    exit(math_ops.maximum(mean_of_square - square_of_mean, 0))
