# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
"""Verifies the gradients of a pooling function.

    Args:
      pool_func: Function to be called, co.MaxPool, co.AvgPool,
        or the Lua version.
      input_sizes: Input tensor dimensions.
      output_sizes: Output tensor dimensions.
      window: Tuple of kernel dims: planes, rows, cols.
      strides: Tuple of strides for dims: planes, rows, cols.
      padding: Padding type.
      data_format: Data format string.
      data_type: The data type to use to run the pooling operation.
      use_gpu: Whether to run on GPU.
    """
jacob_a, jacob_n = self._getJacobians(
    pool_func,
    input_sizes,
    output_sizes,
    window,
    strides,
    padding,
    data_format,
    use_gpu,
    dtype=data_type.as_numpy_dtype)

if data_type == dtypes.bfloat16:
    # Compare bf16 analytical gradients to fp32 numerical gradients.
    _, jacob_n = self._getJacobians(
        pool_func,
        input_sizes,
        output_sizes,
        window,
        strides,
        padding,
        data_format,
        use_gpu,
        dtype=np.float32)

input_jacob_a, grad_jacob_a = jacob_a
input_jacob_n, grad_jacob_n = jacob_n
self.assertAllClose(input_jacob_a, input_jacob_n, rtol=1e-3, atol=1e-3)
self.assertAllClose(grad_jacob_a, grad_jacob_n, rtol=1e-3, atol=1e-3)
