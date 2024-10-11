# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Test when num of rows/cols can evenly divide pooling ratio.

    This is a case regular max pooling can handle. Should be handled by
    fractional pooling as well.
    """
pseudo_random = True
overlapping = True
num_batches = 3
num_channels = 3
num_rows = 30
num_cols = 50
tensor_shape = (num_batches, num_rows, num_cols, num_channels)
# random tensor with value in [-500.0, 500.0)
rand_mat = self._PRNG.random_sample(tensor_shape) * 1000 - 500
self._ValidateFractionalMaxPoolResult(rand_mat, [1, 2, 2, 1], pseudo_random,
                                      overlapping)
