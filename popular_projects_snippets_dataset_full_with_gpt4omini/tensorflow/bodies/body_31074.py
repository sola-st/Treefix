# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
with self.cached_session() as _:
    # Whether turn on `TF2_BEHAVIOR` generates different error messages
    with self.assertRaisesRegex(
        (errors.InvalidArgumentError, ValueError),
        r"(pooling_ratio cannot be smaller than 1, got: .*)|(is negative)"):
        result = nn_ops.gen_nn_ops.fractional_avg_pool(
            value=np.zeros([3, 30, 30, 3]),
            pooling_ratio=[1, -1, 3, 1],
            pseudo_random=False,
            overlapping=False,
            deterministic=False,
            seed=0,
            seed2=0,
        )
        self.evaluate(result)
