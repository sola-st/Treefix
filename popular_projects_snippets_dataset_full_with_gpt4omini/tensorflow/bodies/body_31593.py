# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called, co.MaxPool, co.AvgPool,
        or the Lua version.
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      data_format: The data format we use to run the pooling operation.
      expected: An array containing the expected operation outputs.
      use_gpu: Whether we are running on GPU.
      v2: Whether to use v2 version.
      use_negative_input: If the input values should be negative."
    """
if data_format == "NCHW_VECT_C":
    avg_pool_func = nn_ops.avg_pool
    tf_logging.info("pool_func=%s", pool_func)
    if pool_func == avg_pool_func:
        tf_logging.info("NCHW_VECT_C not yet implemented for avg_pool")
        exit()
    if (self._isMaxPool(pool_func) and isinstance(padding, list)):
        tf_logging.info("NCHW_VECT_C not yet implemented for max pool" +
                        " with explicit padding")
        exit()

self._VerifyOneType(pool_func, input_sizes, ksize, strides, padding,
                    data_format, dtypes.float32, expected, use_gpu, v2,
                    use_negative_input)
if not test.is_built_with_rocm():
    # double datatype is not supported for pooling ops on the ROCm platform
    self._VerifyOneType(pool_func, input_sizes, ksize, strides, padding,
                        data_format, dtypes.float64, expected, use_gpu, v2,
                        use_negative_input)

if not use_gpu or test_util.GpuSupportsHalfMatMulAndConv():
    self._VerifyOneType(pool_func, input_sizes, ksize, strides, padding,
                        data_format, dtypes.float16, expected, use_gpu, v2,
                        use_negative_input)
