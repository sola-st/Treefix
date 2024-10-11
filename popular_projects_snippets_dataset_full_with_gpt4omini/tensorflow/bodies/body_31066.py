# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Try all possible input options for fractional_avg_pool.
    """
num_batches = 5
num_channels = 3
num_rows = 20
num_cols = 30
for pseudo_random in True, False:
    for overlapping in True, False:
        tensor_shape = (num_batches, num_rows, num_cols, num_channels)
        # random tensor with value in [-500.0, 500.0)
        rand_mat = self._PRNG.random_sample(tensor_shape) * 1000 - 500
        self._ValidateFractionalAvgPoolResult(
            rand_mat, [1, math.sqrt(3), math.sqrt(2), 1], pseudo_random,
            overlapping)
