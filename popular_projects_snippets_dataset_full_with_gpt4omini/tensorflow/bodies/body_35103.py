# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
logx_ = np.array([[0., -1, 1000.],
                  [0, 1, -1000.],
                  [-5, 0, 5]])
w_ = np.array([[1., 1, -1],
               [1, -2, 1],
               [1, 0, 1]])
expected, _ = self._reduce_weighted_logsumexp(logx_, w_, axis=-1)
with self.cached_session() as sess:
    logx = constant_op.constant(logx_)
    w = constant_op.constant(w_)
    actual, actual_sgn = du.reduce_weighted_logsumexp(
        logx, w, axis=-1, return_sign=True)
    [actual_, actual_sgn_] = self.evaluate([actual, actual_sgn])
self.assertAllEqual(expected, actual_)
self.assertAllEqual([-1., -1, 1], actual_sgn_)
