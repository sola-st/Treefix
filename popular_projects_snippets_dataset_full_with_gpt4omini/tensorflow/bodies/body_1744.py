# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called, co.MaxPool, co.AvgPool,
        or the Lua version.
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      expected: An array containing the expected operation outputs.
    """
for data_format in GetTestConfigs():
    self._VerifyOneTest(pool_func, input_sizes, ksize, strides, padding,
                        data_format, expected)
