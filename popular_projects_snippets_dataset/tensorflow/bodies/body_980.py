# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
self._assertOpOutputMatchesExpected(
    lambda x: array_ops.bitcast(x, dtypes.int32),
    np.array([1, 0x3f800000], np.int32),
    expected=np.array([1, 0x3f800000], np.int32))
self._assertOpOutputMatchesExpected(
    lambda x: array_ops.bitcast(x, dtypes.float32),
    np.array([1, 0x3f800000], np.int32),
    expected=np.array([1e-45, 1.0], np.float32))
self._assertOpOutputMatchesExpected(
    lambda x: array_ops.bitcast(x, dtypes.int32),
    np.array([1e-45, 1.0], np.float32),
    expected=np.array([1, 0x3f800000], np.int32))
if np.int64 in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        lambda x: array_ops.bitcast(x, dtypes.int64),
        np.array([1, 0x100000003f800000], np.uint64),
        expected=np.array([1, 0x100000003f800000], np.int64))
    self._assertOpOutputMatchesExpected(
        lambda x: array_ops.bitcast(x, dtypes.uint64),
        np.array([1, 0x100000003f800000], np.int64),
        expected=np.array([1, 0x100000003f800000], np.uint64))
