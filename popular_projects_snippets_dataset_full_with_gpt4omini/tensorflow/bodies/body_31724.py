# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called: co.MaxPool, co.AvgPool.
      input_sizes: Input tensor dimensions.
      window: Tuple of kernel dims: planes, rows, cols.
      strides: Tuple of strides for dims: planes, rows, cols.
      padding: Padding type.
      data_format: The data format we use to run the pooling operation.
      data_type: The data type to use to run the pooling operation.
      expected: An array containing the expected operation outputs.
      use_gpu: Whether to run ops on GPU.
    """
total_size = 1
for s in input_sizes:
    total_size *= s
# Initializes the input tensor with array containing incrementing
# numbers from 1.
x = [f * 1.0 for f in range(1, total_size + 1)]
if data_type == dtypes.bfloat16:
    x = [f * 0.1 for f in x]
    expected = [f * 0.1 for f in expected]
with self.cached_session(use_gpu=use_gpu):
    t = constant_op.constant(x, shape=input_sizes, dtype=data_type)
    window = [1] + list(window) + [1]
    strides = [1] + list(strides) + [1]
    if data_format == "NCDHW":
        t = test_util.NHWCToNCHW(t)
        window = test_util.NHWCToNCHW(window)
        strides = test_util.NHWCToNCHW(strides)
    t = pool_func(
        t,
        ksize=window,
        strides=strides,
        padding=padding,
        data_format=data_format)
    if data_format == "NCDHW":
        t = test_util.NCHWToNHWC(t)
    vals = self.evaluate(t)
# Verifies values.
actual = vals.flatten()
rtol = atol = 1e-6
if data_type == dtypes.bfloat16:
    rtol = atol = 2e-2
self.assertAllClose(expected, actual, rtol=rtol, atol=atol)
