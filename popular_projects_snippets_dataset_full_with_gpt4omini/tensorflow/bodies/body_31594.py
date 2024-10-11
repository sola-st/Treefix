# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called, co.MaxPool, co.AvgPool,
        or the Lua version.
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      expected: An array containing the expected operation outputs.
      use_gpu: Whether we are running on GPU.
      v2: Whether to use v2 version.
      one_dim: If one dimensional pools should be done instead of two
        dimensional pools.
      use_negative_input: If the input values should be negative.
    """
for (data_format, use_gpu_2) in GetTestConfigs(
    include_nchw_vect_c=True, one_dimensional=one_dim):
    if use_gpu_2 == use_gpu:
        self._VerifyOneTest(pool_func, input_sizes, ksize, strides, padding,
                            data_format, expected, use_gpu, v2,
                            use_negative_input)
