# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    # Note that this range contains both zero and inf.
    x = constant_op.constant(np.logspace(-8, 6).astype(np.float16))
    y = du.softplus_inverse(x)
    grads = self.evaluate(gradients_impl.gradients(y, x)[0])
    # Equivalent to `assertAllFalse` (if it existed).
    self.assertAllEqual(
        np.zeros_like(grads).astype(np.bool_), np.isnan(grads))
