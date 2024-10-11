# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
with self.cached_session(use_gpu=use_gpu):
    x = ops.convert_to_tensor(x, dtype=dtype)

    result_naive, result_fused = self.evaluate(
        self._computeLogSumExp(x, **kwargs))

tol = 2e-2 if dtype in [dtypes.float16, dtypes.bfloat16] else 1e-6
self.assertAllClose(result_naive, result_fused, rtol=tol, atol=tol)
