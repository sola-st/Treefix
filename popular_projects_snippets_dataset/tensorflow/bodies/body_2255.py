# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
self._testBinary(
    math_ops.logical_and,
    np.array([[True, False], [False, True]], dtype=np.bool_),
    np.array([[False, True], [False, True]], dtype=np.bool_),
    expected=np.array([[False, False], [False, True]], dtype=np.bool_))

self._testBinary(
    math_ops.logical_or,
    np.array([[True, False], [False, True]], dtype=np.bool_),
    np.array([[False, True], [False, True]], dtype=np.bool_),
    expected=np.array([[True, True], [False, True]], dtype=np.bool_))
