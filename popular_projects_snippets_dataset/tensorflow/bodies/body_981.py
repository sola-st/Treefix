# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
self._assertOpOutputMatchesExpected(
    lambda x: array_ops.bitcast(x, dtypes.float32),
    np.array([[1, 0, 0, 0], [0xd0, 0x0f, 0x49, 0x40]], np.int8),
    expected=np.array([1e-45, 3.14159], np.float32))
self._assertOpOutputMatchesExpected(
    lambda x: array_ops.bitcast(x, dtypes.np.int8),
    np.array([1e-45, 3.14159], np.float32),
    expected=np.array([[1, 0, 0, 0], [0xd0, 0x0f, 0x49, 0x40]], np.int8))
