# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Test case for GitHub issue 46700.
for dtype, reductions in [
    (dtypes.float32, (math_ops.reduce_sum, math_ops.reduce_mean,
                      math_ops.reduce_prod, math_ops.reduce_max,
                      math_ops.reduce_min, math_ops.reduce_euclidean_norm)),
    (dtypes.bool, (math_ops.reduce_all, math_ops.reduce_any))
]:
    for reduction in reductions:
        with self.assertRaisesRegex(ValueError, "The truth value"):
            x = True if dtype == dtypes.bool else 1
            y = reduction(
                input_tensor=x, keepdims=np.array([63600, 1], dtype=np.float16))
            self.evaluate(y)
