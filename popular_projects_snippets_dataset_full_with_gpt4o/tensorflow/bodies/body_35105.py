# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
"""This test verifies the correctness of the docstring examples."""

with self.cached_session():
    x = constant_op.constant([[0., 0, 0],
                              [0, 0, 0]])

    w = constant_op.constant([[-1., 1, 1],
                              [1, 1, 1]])

    self.assertAllClose(
        np.log(4), self.evaluate(du.reduce_weighted_logsumexp(x, w)))

    with np.errstate(divide="ignore"):
        self.assertAllClose(
            np.log([0, 2, 2]),
            self.evaluate(du.reduce_weighted_logsumexp(x, w, axis=0)))

    self.assertAllClose(
        np.log([1, 3]),
        self.evaluate(du.reduce_weighted_logsumexp(x, w, axis=1)))

    self.assertAllClose(
        np.log([[1], [3]]),
        self.evaluate(
            du.reduce_weighted_logsumexp(x, w, axis=1, keep_dims=True)))

    self.assertAllClose(
        np.log(4),
        self.evaluate(du.reduce_weighted_logsumexp(x, w, axis=[0, 1])))
