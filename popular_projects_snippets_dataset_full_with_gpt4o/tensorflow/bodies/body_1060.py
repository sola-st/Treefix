# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nullary_ops_test.py
for dtype in self.numeric_types:
    constants = [
        dtype(42),
        np.array([], dtype=dtype),
        np.array([1, 2], dtype=dtype),
        np.array([7, 7, 7, 7, 7], dtype=dtype),
        np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype),
        np.array([[[1, 2], [3, 4], [5, 6]], [[10, 20], [30, 40], [50, 60]]],
                 dtype=dtype),
        np.array([[[]], [[]]], dtype=dtype),
        np.array([[[[1]]]], dtype=dtype),
    ]
    for c in constants:
        self._testNullary(lambda c=c: constant_op.constant(c), expected=c)
