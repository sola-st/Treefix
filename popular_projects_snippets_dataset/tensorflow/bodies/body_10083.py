# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
with test_util.use_gpu():
    res = math_ops.reduce_logsumexp(-np.inf)
    self.assertEqual(-np.inf, self.evaluate(res))
