# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nullary_ops_test.py
for dtype in self.complex_types:
    constants = [
        dtype(42 + 3j),
        np.array([], dtype=dtype),
        np.ones([50], dtype=dtype) * (3 + 4j),
        np.array([1j, 2 + 1j], dtype=dtype),
        np.array([[1, 2j, 7j], [4, 5, 6]], dtype=dtype),
        np.array([[[1, 2], [3, 4 + 6j], [5, 6]],
                  [[10 + 7j, 20], [30, 40], [50, 60]]],
                 dtype=dtype),
        np.array([[[]], [[]]], dtype=dtype),
        np.array([[[[1 + 3j]]]], dtype=dtype),
    ]
    for c in constants:
        self._testNullary(lambda c=c: constant_op.constant(c), expected=c)
