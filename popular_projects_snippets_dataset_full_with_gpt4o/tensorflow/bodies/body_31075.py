# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
with self.cached_session() as _:
    with self.assertRaises(errors.UnimplementedError):
        result = nn_ops.gen_nn_ops.fractional_avg_pool(
            np.zeros([3, 30, 50, 3]),
            [2, 3, 1.5, 1],
            True,
            True)
        self.evaluate(result)
