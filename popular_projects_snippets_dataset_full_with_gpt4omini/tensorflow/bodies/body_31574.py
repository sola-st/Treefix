# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
tensor_shape = (5, 20, 20, 3)
rand_mat = self._PRNG.random_sample(tensor_shape) * 1000 - 500
with test_util.deterministic_ops():
    with self.assertRaisesRegex(
        ValueError, "requires a non-zero seed to be passed in when "
        "determinism is enabled"):
        nn_ops.fractional_max_pool_v2(rand_mat, [1, 1.5, 1.5, 1])
    nn_ops.fractional_max_pool_v2(rand_mat, [1, 1.5, 1.5, 1], seed=1)

    with self.assertRaisesRegex(ValueError,
                                'requires "seed" and "seed2" to be non-zero'):
        nn_ops.fractional_max_pool(rand_mat, [1, 1.5, 1.5, 1])
    nn_ops.fractional_max_pool(
        rand_mat, [1, 1.5, 1.5, 1], seed=1, seed2=1, deterministic=True)
