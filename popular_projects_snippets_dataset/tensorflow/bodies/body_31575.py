# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
with self.cached_session() as _:
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"Pooling ratio is higher than input dimension size for dimension 1.*"
    ):
        result = nn_ops.gen_nn_ops.fractional_max_pool(
            value=constant_op.constant(
                value=[[[[1, 4, 2, 3]]]], dtype=dtypes.int64),
            pooling_ratio=[1.0, 1.44, 1.73, 1.0],
            pseudo_random=False,
            overlapping=False,
            deterministic=False,
            seed=0,
            seed2=0,
            name=None)
        self.evaluate(result)
