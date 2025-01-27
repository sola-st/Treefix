# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Test it works fine when input tensor is integer type.
    """
num_batches = 5
num_channels = 3
num_rows = 20
num_cols = 30
pseudo_random = True
overlapping = True
tensor_shape = (num_batches, num_rows, num_cols, num_channels)
rand_mat = self._PRNG.randint(1000, size=tensor_shape)
self._ValidateFractionalMaxPoolResult(rand_mat,
                                      [1, math.sqrt(3), math.sqrt(2), 1],
                                      pseudo_random, overlapping)
