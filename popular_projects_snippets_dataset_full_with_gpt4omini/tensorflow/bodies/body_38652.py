# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
# This test ensures that the operation is correct even when the naive
# implementation would overflow.
x_np = np.arange(20) * 20.0

for use_gpu in (True, False):
    with self.cached_session(use_gpu=use_gpu):
        x_tf = ops.convert_to_tensor(x_np, dtype=dtypes.float32)

        result_fused = self.evaluate(math_ops.cumulative_logsumexp(x_tf))
        result_map = self.evaluate(self._logSumExpMap(x_tf))

    self.assertAllClose(result_fused, result_map)
