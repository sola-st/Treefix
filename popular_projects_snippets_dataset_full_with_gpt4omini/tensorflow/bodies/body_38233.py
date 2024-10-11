# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.session():
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([1, 1, 1, 2, 2, 3])),
        [0, 3, 2, 1])
    arr = [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount(arr)), [0, 5, 4, 3, 2, 1])
    arr += [0, 0, 0, 0, 0, 0]
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount(arr)), [6, 5, 4, 3, 2, 1])

    self.assertAllEqual(self.evaluate(bincount_ops.bincount([])), [])
    self.assertAllEqual(self.evaluate(bincount_ops.bincount([0, 0, 0])), [3])
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([5])), [0, 0, 0, 0, 0, 1])
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount(np.arange(10000))),
        np.ones(10000))
