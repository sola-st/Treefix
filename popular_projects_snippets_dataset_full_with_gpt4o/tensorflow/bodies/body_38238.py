# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.session():
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount(np.arange(1000), np.zeros(1000))),
        np.zeros(1000))
