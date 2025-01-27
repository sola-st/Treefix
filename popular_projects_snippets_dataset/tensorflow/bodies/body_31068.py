# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Test different shapes of input tensor.

    Mainly test different combinations of num_rows and num_cols.
    """
pseudo_random = True
overlapping = True
for num_batches in [1, 3]:
    for num_channels in [1, 3]:
        for num_rows in [10, 20, 50]:
            for num_cols in [10, 20, 50]:
                tensor_shape = (num_batches, num_rows, num_cols, num_channels)
                # random tensor with value in [-500.0, 500.0)
                rand_mat = self._PRNG.random_sample(tensor_shape) * 1000 - 500
                self._ValidateFractionalAvgPoolResult(
                    rand_mat, [1, math.sqrt(3), math.sqrt(2), 1], pseudo_random,
                    overlapping)
