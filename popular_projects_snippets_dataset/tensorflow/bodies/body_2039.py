# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
self._assertOpOutputMatchesExpected(
    xla.shift_right_arithmetic,
    args=(np.array([-1, 16], dtype=np.int32), np.int32(4)),
    expected=np.array([-1, 1], dtype=np.int32))

self._assertOpOutputMatchesExpected(
    xla.shift_right_arithmetic,
    args=(np.array([0xFFFFFFFF, 16], dtype=np.uint32), np.uint32(4)),
    expected=np.array([0xFFFFFFFF, 1], dtype=np.uint32))
