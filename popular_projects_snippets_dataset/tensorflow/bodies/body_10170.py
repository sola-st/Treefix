# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
shape = (24, 8)
for dtype in self._getValidDtypes():
    tf_values = self._generateRandomTensor(dtype, shape)
    np_values = self.evaluate(tf_values)
    for axis in range(0, len(shape)):
        np_min = np.argmin(np_values, axis=axis)
        tf_min = math_ops.argmin(tf_values, axis=axis)
        self.assertAllEqual(tf_min, np_min)
