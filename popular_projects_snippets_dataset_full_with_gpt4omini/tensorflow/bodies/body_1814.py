# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
for dtype in self.complex_types:
    self._testNAry(
        math_ops.add_n, [np.array([[1 + 2j, 2 - 3j, 3 + 4j]], dtype=dtype)],
        expected=np.array([[1 + 2j, 2 - 3j, 3 + 4j]], dtype=dtype))

    self._testNAry(
        math_ops.add_n, [
            np.array([1 + 2j, 2 - 3j], dtype=dtype),
            np.array([10j, 20], dtype=dtype)
        ],
        expected=np.array([1 + 12j, 22 - 3j], dtype=dtype))
    self._testNAry(
        math_ops.add_n, [
            np.array([-4, 5j], dtype=dtype),
            np.array([2 + 10j, -2], dtype=dtype),
            np.array([42j, 3 + 3j], dtype=dtype)
        ],
        expected=np.array([-2 + 52j, 1 + 8j], dtype=dtype))
