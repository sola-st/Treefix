# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        math_ops.subtract,
        np.array([1, 2, 100], dtype=dtype),
        np.array([10, 20, -1], dtype=dtype),
        expected=np.array([-9, -18, 101], dtype=dtype))
    self._testBinary(
        math_ops.subtract,
        dtype(5),
        np.array([1, 2], dtype=dtype),
        expected=np.array([4, 3], dtype=dtype))
    self._testBinary(
        math_ops.subtract,
        np.array([[1], [2]], dtype=dtype),
        dtype(7),
        expected=np.array([[-6], [-5]], dtype=dtype))

    # min/max not supported for complex
    if dtype not in self.complex_types | {np.uint8, np.int8}:
        self._testBinary(
            math_ops.maximum,
            np.array([1, 2], dtype=dtype),
            np.array([10, 20], dtype=dtype),
            expected=np.array([10, 20], dtype=dtype))
        self._testBinary(
            math_ops.maximum,
            dtype(5),
            np.array([1, 20], dtype=dtype),
            expected=np.array([5, 20], dtype=dtype))
        self._testBinary(
            math_ops.maximum,
            np.array([[10], [2]], dtype=dtype),
            dtype(7),
            expected=np.array([[10], [7]], dtype=dtype))

        self._testBinary(
            math_ops.minimum,
            np.array([1, 20], dtype=dtype),
            np.array([10, 2], dtype=dtype),
            expected=np.array([1, 2], dtype=dtype))
        self._testBinary(
            math_ops.minimum,
            dtype(5),
            np.array([1, 20], dtype=dtype),
            expected=np.array([1, 5], dtype=dtype))
        self._testBinary(
            math_ops.minimum,
            np.array([[10], [2]], dtype=dtype),
            dtype(7),
            expected=np.array([[7], [2]], dtype=dtype))

    # Complex support for squared_difference is incidental, see b/68205550
    if dtype not in self.complex_types | {np.uint8, np.int8}:
        self._testBinary(
            math_ops.squared_difference,
            np.array([1, 2], dtype=dtype),
            np.array([10, 20], dtype=dtype),
            expected=np.array([81, 324], dtype=dtype))
        self._testBinary(
            math_ops.squared_difference,
            dtype(5),
            np.array([1, 2], dtype=dtype),
            expected=np.array([16, 9], dtype=dtype))
        self._testBinary(
            math_ops.squared_difference,
            np.array([[1], [2]], dtype=dtype),
            dtype(7),
            expected=np.array([[36], [25]], dtype=dtype))

    self._testBinary(
        nn_ops.bias_add,
        np.array([[1, 2], [3, 4]], dtype=dtype),
        np.array([2, -1], dtype=dtype),
        expected=np.array([[3, 1], [5, 3]], dtype=dtype))
    self._testBinary(
        nn_ops.bias_add,
        np.array([[[[1, 2], [3, 4]]]], dtype=dtype),
        np.array([2, -1], dtype=dtype),
        expected=np.array([[[[3, 1], [5, 3]]]], dtype=dtype))

if np.int64 in self.numeric_types:
    self._testBinary(
        math_ops.add,
        np.array([0xffffffff, 0xfffffffff, 1, 1], dtype=np.int64),
        np.array([1, 1, 0xffffffff, 0xfffffffff], dtype=np.int64),
        expected=np.array([1 << 32, 1 << 36, 1 << 32, 1 << 36],
                          dtype=np.int64))
