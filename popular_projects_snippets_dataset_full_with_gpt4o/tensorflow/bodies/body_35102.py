# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
logx_ = np.array([[0., -1, 1000.],
                  [0, 1, -1000.],
                  [-5, 0, 5]])
with self.cached_session() as sess:
    logx = constant_op.constant(logx_)
    expected = math_ops.reduce_logsumexp(logx, axis=-1)
    grad_expected = gradients_impl.gradients(expected, logx)[0]
    actual, actual_sgn = du.reduce_weighted_logsumexp(
        logx, axis=-1, return_sign=True)
    grad_actual = gradients_impl.gradients(actual, logx)[0]
    [actual_, actual_sgn_, grad_actual_,
     expected_, grad_expected_] = sess.run([
         actual, actual_sgn, grad_actual,
         expected, grad_expected])
self.assertAllEqual(expected_, actual_)
self.assertAllEqual(grad_expected_, grad_actual_)
self.assertAllEqual([1., 1, 1], actual_sgn_)
