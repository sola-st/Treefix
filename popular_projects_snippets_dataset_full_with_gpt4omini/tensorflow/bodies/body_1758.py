# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Pooling function to be called, e.g., tf.nn.max_pool2d
      pool_grad_func: Corresponding pooling gradient function.
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      pool_grad_grad_func: Second-order gradient function, if available.
    """
for data_format in GetTestConfigs():
    self._VerifyOneTest(
        pool_func,
        pool_grad_func,
        input_sizes,
        ksize,
        strides,
        padding,
        data_format,
        pool_grad_grad_func=pool_grad_grad_func)
