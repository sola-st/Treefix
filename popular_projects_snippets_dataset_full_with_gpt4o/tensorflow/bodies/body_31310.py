# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
"""Numpy implementation of pooling.

  This is intended for testing only, and therefore isn't particularly efficient.

  See tensorflow.nn.pool.

  Args:
    input: numpy array of rank N+2.
    window_shape: Sequence of N ints >= 1.
    pooling_type: either "MAX" or "AVG".
    padding: either "SAME" or "VALID".
    dilation_rate: Sequence of N ints >= 1.
    strides: Sequence of N ints >= 1.
    data_format: If specified and starts with "NC", indicates that second
      dimension, rather than the last dimension, specifies the channel.

  Returns:
    pooling output array of rank N+2.

  Raises:
    ValueError: if arguments are invalid.
  """
if data_format is None or not data_format.startswith("NC"):
    spatial_start_dim = 1
else:
    spatial_start_dim = 2
output = input
for i in range(len(window_shape)):
    output = pool_direct_single_axis(
        input=output,
        axis=i + spatial_start_dim,
        window_size=window_shape[i],
        pooling_type=pooling_type,
        padding=padding,
        dilation_rate=dilation_rate[i],
        stride=strides[i])
exit(output)
