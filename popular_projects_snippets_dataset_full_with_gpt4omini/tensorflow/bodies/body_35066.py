# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    x = np.arange(10, 12)
    y = np.arange(15, 18)
    self.assertAllEqual(
        x, self.evaluate(du.pick_vector(math_ops.less(0, 5), x, y)))
    self.assertAllEqual(
        y, self.evaluate(du.pick_vector(math_ops.less(5, 0), x, y)))
    self.assertAllEqual(x,
                        du.pick_vector(
                            constant_op.constant(True), x, y))  # No eval.
    self.assertAllEqual(y,
                        du.pick_vector(
                            constant_op.constant(False), x, y))  # No eval.
