# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    # This range of x is all finite, and so is 1 / x.  So the
    # gradient and its approximations should be finite as well.
    x = constant_op.constant(np.logspace(-4.8, 4.5).astype(np.float16))
    y = du.softplus_inverse(x)
    grads = self.evaluate(gradients_impl.gradients(y, x)[0])
    # Equivalent to `assertAllTrue` (if it existed).
    self.assertAllEqual(
        np.ones_like(grads).astype(np.bool_), np.isfinite(grads))
