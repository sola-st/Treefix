# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
with self.cached_session():
    for dtype, reductions in [(dtypes.float32,
                               (math_ops.reduce_sum, math_ops.reduce_mean,
                                math_ops.reduce_prod, math_ops.reduce_max,
                                math_ops.reduce_min,
                                math_ops.reduce_euclidean_norm)),
                              (dtypes.bool, (math_ops.reduce_all,
                                             math_ops.reduce_any))]:
        for reduction in reductions:
            x = array_ops.placeholder(
                dtype=dtype, shape=None)  # Some tensor w/ unknown shape.
            y = reduction(x)
            self.assertEqual(y.shape, ())
