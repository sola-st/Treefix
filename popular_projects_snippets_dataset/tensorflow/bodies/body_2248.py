# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.complex_types:
    self._testBinary(
        math_ops.add,
        np.array([1 + 3j, 2 + 7j], dtype=dtype),
        np.array([10 - 4j, 20 + 17j], dtype=dtype),
        expected=np.array([11 - 1j, 22 + 24j], dtype=dtype))
    self._testBinary(
        math_ops.add,
        dtype(5 - 7j),
        np.array([1 + 2j, 2 + 4j], dtype=dtype),
        expected=np.array([6 - 5j, 7 - 3j], dtype=dtype))
    self._testBinary(
        math_ops.add,
        np.array([[1 - 2j], [2 + 1j]], dtype=dtype),
        dtype(7 + 5j),
        expected=np.array([[8 + 3j], [9 + 6j]], dtype=dtype))

    self._testBinary(
        math_ops.subtract,
        np.array([1 + 3j, 2 + 7j], dtype=dtype),
        np.array([10 - 4j, 20 + 17j], dtype=dtype),
        expected=np.array([-9 + 7j, -18 - 10j], dtype=dtype))
    self._testBinary(
        math_ops.subtract,
        dtype(5 - 7j),
        np.array([1 + 2j, 2 + 4j], dtype=dtype),
        expected=np.array([4 - 9j, 3 - 11j], dtype=dtype))
    self._testBinary(
        math_ops.subtract,
        np.array([[1 - 2j], [2 + 1j]], dtype=dtype),
        dtype(7 + 5j),
        expected=np.array([[-6 - 7j], [-5 - 4j]], dtype=dtype))

    self._testBinary(
        math_ops.multiply,
        np.array([1 + 3j, 2 + 7j], dtype=dtype),
        np.array([10 - 4j, 20 + 17j], dtype=dtype),
        expected=np.array([(1 + 3j) * (10 - 4j), (2 + 7j) * (20 + 17j)],
                          dtype=dtype))
    self._testBinary(
        math_ops.multiply,
        dtype(5 - 7j),
        np.array([1 + 2j, 2 + 4j], dtype=dtype),
        expected=np.array([(5 - 7j) * (1 + 2j), (5 - 7j) * (2 + 4j)],
                          dtype=dtype))
    self._testBinary(
        math_ops.multiply,
        np.array([[1 - 2j], [2 + 1j]], dtype=dtype),
        dtype(7 + 5j),
        expected=np.array([[(7 + 5j) * (1 - 2j)], [(7 + 5j) * (2 + 1j)]],
                          dtype=dtype))

    self._testBinary(
        math_ops.div,
        np.array([8 - 1j, 2 + 16j], dtype=dtype),
        np.array([2 + 4j, 4 - 8j], dtype=dtype),
        expected=np.array([(8 - 1j) / (2 + 4j), (2 + 16j) / (4 - 8j)],
                          dtype=dtype))
    self._testBinary(
        math_ops.div,
        dtype(1 + 2j),
        np.array([2 + 4j, 4 - 8j], dtype=dtype),
        expected=np.array([(1 + 2j) / (2 + 4j), (1 + 2j) / (4 - 8j)],
                          dtype=dtype))
    self._testBinary(
        math_ops.div,
        np.array([2 + 4j, 4 - 8j], dtype=dtype),
        dtype(1 + 2j),
        expected=np.array([(2 + 4j) / (1 + 2j), (4 - 8j) / (1 + 2j)],
                          dtype=dtype))

    # TODO(b/68205550): math_ops.squared_difference shouldn't be supported.

    self._testBinary(
        nn_ops.bias_add,
        np.array([[1 + 2j, 2 + 7j], [3 - 5j, 4 + 2j]], dtype=dtype),
        np.array([2 + 6j, -1 - 3j], dtype=dtype),
        expected=np.array([[3 + 8j, 1 + 4j], [5 + 1j, 3 - 1j]], dtype=dtype))
    self._testBinary(
        nn_ops.bias_add,
        np.array([[[[1 + 4j, 2 - 1j], [3 + 7j, 4]]]], dtype=dtype),
        np.array([2 + 1j, -1 + 2j], dtype=dtype),
        expected=np.array([[[[3 + 5j, 1 + 1j], [5 + 8j, 3 + 2j]]]],
                          dtype=dtype))
