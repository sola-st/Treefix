# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
"""Verifies the output shape of the max pooling function when tensor is empty.

    Args: none
    """
input_sizes = [0, 112, 112, 112, 64]

input_data = 1.
input_tensor = constant_op.constant(
    input_data, shape=input_sizes, name="input")
max_pool_3d = nn_ops.max_pool3d(
    input_tensor,
    ksize=[2, 2, 2],
    strides=[2, 2, 2],
    padding="VALID",
    data_format="NDHWC",
    name="max_pool_3d")
values = self.evaluate(max_pool_3d)
self.assertEqual(values.shape, (0, 56, 56, 56, 64))
