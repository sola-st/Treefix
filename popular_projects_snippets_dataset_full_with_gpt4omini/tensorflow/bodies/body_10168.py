# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in self._getValidDtypes():
    values = constant_op.constant(
        [[10, 11, 15, 15, 10], [12, 12, 10, 10, 12]], dtype=dtype)
    self.assertAllEqual(
        math_ops.argmax(values, axis=1),
        np.argmax(self.evaluate(values), axis=1))

    # Long tensor to ensure works with multithreading/GPU
    values = array_ops.zeros(shape=(193681,), dtype=dtype)
    self.assertAllEqual(math_ops.argmax(values), 0)
