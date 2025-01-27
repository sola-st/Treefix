# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.session():
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([], minlength=5)),
        [0, 0, 0, 0, 0])
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([], minlength=1)), [0])
    self.assertAllEqual(
        self.evaluate(bincount_ops.bincount([], minlength=0)), [])
    self.assertEqual(
        self.evaluate(
            bincount_ops.bincount([], minlength=0, dtype=np.float32)).dtype,
        np.float32)
    self.assertEqual(
        self.evaluate(
            bincount_ops.bincount([], minlength=3, dtype=np.float64)).dtype,
        np.float64)
