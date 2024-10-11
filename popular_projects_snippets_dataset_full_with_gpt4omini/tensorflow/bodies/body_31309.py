# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
"""Numpy implementation of pooling along a single axis.

  This is intended for testing only, and therefore isn't particularly efficient.

  See pool_direct below for the meaning of the arguments.

  Args:
    input: numpy array.
    axis: axis along which to perform pooling.
    window_size: int >= 1.  Size of pooling window within axis.
    pooling_type: either "MAX" or "AVG".
    padding: either "SAME" or "VALID".
    dilation_rate: int >= 1.  Dilation factor for window, i.e. stride at which
      to sample input.
    stride: int >= 1.  Stride at which to generate output.

  Returns:
    pooling output array of rank N+2.

  Raises:
    ValueError: if arguments are invalid.
  """
effective_window_size = (window_size - 1) * dilation_rate + 1
input_size = input.shape[axis]
if padding == "SAME":
    output_size = int(math.ceil(input_size / stride))
    total_padding_amount = max(0, (output_size - 1) * stride +
                               effective_window_size - input_size)
    before_padding = total_padding_amount // 2
elif padding == "VALID":
    output_size = int(
        math.ceil((input_size - effective_window_size + 1) / stride))
    before_padding = 0
else:
    raise ValueError("Unsupported padding type: %r" % (padding,))

output_shape = input.shape[:axis] + (output_size,) + input.shape[axis + 1:]
output = np.zeros(output_shape, input.dtype)
initial_dim_selector = tuple(np.s_[:] for _ in range(axis))
if pooling_type == "MAX":
    pooling_func = np.max
elif pooling_type == "AVG":
    pooling_func = np.mean
else:
    raise ValueError("Unsupported pooling type: %r" % (pooling_type,))
for output_pos in range(output_size):
    input_start_pos = output_pos * stride - before_padding
    input_end_pos = min(input_start_pos + effective_window_size, input_size)
    if input_start_pos < 0:
        input_start_pos += dilation_rate
    input_slice = np.s_[input_start_pos:input_end_pos:dilation_rate]

    output[initial_dim_selector + (output_pos,)] = pooling_func(
        input[initial_dim_selector + (input_slice,)], axis=axis)
exit(output)
