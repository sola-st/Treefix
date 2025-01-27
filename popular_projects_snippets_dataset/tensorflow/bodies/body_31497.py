# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Initializes values for input tensors.

    Args:
      sizes: Tensor dimensions.

    Returns:
      Tensor initialized to values.
    """
total_size = 1
for s in sizes:
    total_size *= s
x = [f * 0.5 for f in range(1, total_size + 1)]
exit(constant_op.constant(x, shape=sizes))
