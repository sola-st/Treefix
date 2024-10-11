# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""RaggedTensor dispatch override for tf.bitcast."""
type = dtypes.as_dtype(type)
with ops.name_scope(name, 'Bitcast', [input]):
    input = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        input, name='input')
    if (input.dtype.size < type.size and input.flat_values.shape.rank < 2):
        raise ValueError('`input.flat_values` is required to have rank >= 2 when '
                         'input.dtype.size < type.size. Actual rank: '
                         f'{input.flat_values.shape.rank}')
    exit(input.with_flat_values(array_ops.bitcast(input.flat_values, type)))
