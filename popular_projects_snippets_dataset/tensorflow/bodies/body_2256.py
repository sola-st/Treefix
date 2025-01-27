# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
self._testBinary(
    math_ops.equal,
    np.array([1, 5, 20], dtype=np.float32),
    np.array([10, 5, 2], dtype=np.float32),
    expected=np.array([False, True, False], dtype=np.bool_))
self._testBinary(
    math_ops.equal,
    np.float32(5),
    np.array([1, 5, 20], dtype=np.float32),
    expected=np.array([False, True, False], dtype=np.bool_))
self._testBinary(
    math_ops.equal,
    np.array([[10], [7], [2]], dtype=np.float32),
    np.float32(7),
    expected=np.array([[False], [True], [False]], dtype=np.bool_))

self._testBinary(
    math_ops.not_equal,
    np.array([1, 5, 20], dtype=np.float32),
    np.array([10, 5, 2], dtype=np.float32),
    expected=np.array([True, False, True], dtype=np.bool_))
self._testBinary(
    math_ops.not_equal,
    np.float32(5),
    np.array([1, 5, 20], dtype=np.float32),
    expected=np.array([True, False, True], dtype=np.bool_))
self._testBinary(
    math_ops.not_equal,
    np.array([[10], [7], [2]], dtype=np.float32),
    np.float32(7),
    expected=np.array([[True], [False], [True]], dtype=np.bool_))

for greater_op in [math_ops.greater, (lambda x, y: x > y)]:
    self._testBinary(
        greater_op,
        np.array([1, 5, 20], dtype=np.float32),
        np.array([10, 5, 2], dtype=np.float32),
        expected=np.array([False, False, True], dtype=np.bool_))
    self._testBinary(
        greater_op,
        np.float32(5),
        np.array([1, 5, 20], dtype=np.float32),
        expected=np.array([True, False, False], dtype=np.bool_))
    self._testBinary(
        greater_op,
        np.array([[10], [7], [2]], dtype=np.float32),
        np.float32(7),
        expected=np.array([[True], [False], [False]], dtype=np.bool_))

for greater_equal_op in [math_ops.greater_equal, (lambda x, y: x >= y)]:
    self._testBinary(
        greater_equal_op,
        np.array([1, 5, 20], dtype=np.float32),
        np.array([10, 5, 2], dtype=np.float32),
        expected=np.array([False, True, True], dtype=np.bool_))
    self._testBinary(
        greater_equal_op,
        np.float32(5),
        np.array([1, 5, 20], dtype=np.float32),
        expected=np.array([True, True, False], dtype=np.bool_))
    self._testBinary(
        greater_equal_op,
        np.array([[10], [7], [2]], dtype=np.float32),
        np.float32(7),
        expected=np.array([[True], [True], [False]], dtype=np.bool_))

for less_op in [math_ops.less, (lambda x, y: x < y)]:
    self._testBinary(
        less_op,
        np.array([1, 5, 20], dtype=np.float32),
        np.array([10, 5, 2], dtype=np.float32),
        expected=np.array([True, False, False], dtype=np.bool_))
    self._testBinary(
        less_op,
        np.float32(5),
        np.array([1, 5, 20], dtype=np.float32),
        expected=np.array([False, False, True], dtype=np.bool_))
    self._testBinary(
        less_op,
        np.array([[10], [7], [2]], dtype=np.float32),
        np.float32(7),
        expected=np.array([[False], [False], [True]], dtype=np.bool_))
    if np.int64 in self.numeric_types:
        self._testBinary(
            less_op,
            np.array([[10], [7], [2], [-1]], dtype=np.int64),
            np.int64(7),
            expected=np.array([[False], [False], [True], [True]],
                              dtype=np.bool_))

for less_equal_op in [math_ops.less_equal, (lambda x, y: x <= y)]:
    self._testBinary(
        less_equal_op,
        np.array([1, 5, 20], dtype=np.float32),
        np.array([10, 5, 2], dtype=np.float32),
        expected=np.array([True, True, False], dtype=np.bool_))
    self._testBinary(
        less_equal_op,
        np.float32(5),
        np.array([1, 5, 20], dtype=np.float32),
        expected=np.array([False, True, True], dtype=np.bool_))
    self._testBinary(
        less_equal_op,
        np.array([[10], [7], [2]], dtype=np.float32),
        np.float32(7),
        expected=np.array([[False], [True], [True]], dtype=np.bool_))
