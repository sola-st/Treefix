# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
self._assertOpOutputMatchesExpected(
    math_ops.logical_not,
    np.array([[True, False], [False, True]], dtype=np.bool_),
    expected=np.array([[False, True], [True, False]], dtype=np.bool_))
