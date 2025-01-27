# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
self._testTernary(
    math_ops.range,
    np.int32(1),
    np.int32(2),
    np.int32(1),
    expected=np.array([1], dtype=np.int32))
self._testTernary(
    math_ops.range,
    np.int32(1),
    np.int32(7),
    np.int32(2),
    expected=np.array([1, 3, 5], dtype=np.int32))
