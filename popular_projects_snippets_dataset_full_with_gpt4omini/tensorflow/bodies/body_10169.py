# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
shape = (24, 8)
for dtype in self._getValidDtypes():
    tf_values = self._generateRandomTensor(dtype, shape)
    np_values = self.evaluate(tf_values)
    for axis in range(0, len(shape)):
        np_max = np.argmax(np_values, axis=axis)
        tf_max = math_ops.argmax(
            tf_values, axis=axis, output_type=dtypes.uint16)
        self.assertAllEqual(tf_max, np_max)
