# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Test when pooling ratio is not within [1, 2).
    """
pseudo_random = True
overlapping = True
num_batches = 3
num_channels = 3
num_rows = 30
num_cols = 50
tensor_shape = (num_batches, num_rows, num_cols, num_channels)
for row_ratio in [math.sqrt(11), math.sqrt(37)]:
    for col_ratio in [math.sqrt(11), math.sqrt(27)]:
        # random tensor with value in [-500.0, 500.0)
        rand_mat = self._PRNG.random_sample(tensor_shape) * 1000 - 500
        self._ValidateFractionalAvgPoolResult(rand_mat,
                                              [1, row_ratio, col_ratio, 1],
                                              pseudo_random, overlapping)
