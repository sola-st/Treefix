# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
"""Direct Python implementation of space-to-batch conversion.

  This is used for tests only.

  Args:
    input_array: N-D array
    block_shape: 1-D array of shape [num_block_dims].
    paddings: 2-D array of shape [num_block_dims, 2].

  Returns:
    Converted tensor.
  """
input_array = np.array(input_array)
block_shape = np.array(block_shape)
num_block_dims = len(block_shape)
paddings = np.array(paddings).reshape((len(block_shape), 2))

padded = np.pad(input_array,
                pad_width=([[0, 0]] + list(paddings) + [[0, 0]] *
                           (input_array.ndim - 1 - num_block_dims)),
                mode="constant")
reshaped_padded_shape = [input_array.shape[0]]
output_shape = [input_array.shape[0] * np.prod(block_shape)]
for block_dim, block_shape_value in enumerate(block_shape):
    reduced_size = padded.shape[block_dim + 1] // block_shape_value
    reshaped_padded_shape.append(reduced_size)
    output_shape.append(reduced_size)
    reshaped_padded_shape.append(block_shape_value)
reshaped_padded_shape.extend(input_array.shape[num_block_dims + 1:])
output_shape.extend(input_array.shape[num_block_dims + 1:])

reshaped_padded = padded.reshape(reshaped_padded_shape)
permuted_reshaped_padded = np.transpose(reshaped_padded, (
    list(np.arange(num_block_dims) * 2 + 2) + [0] +
    list(np.arange(num_block_dims) * 2 + 1) + list(
        np.arange(input_array.ndim - num_block_dims - 1) + 1 + num_block_dims
        * 2)))
exit(permuted_reshaped_padded.reshape(output_shape))
