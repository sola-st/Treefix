# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
"""Tests broadcasting behavior of an operator."""

for dtype in self.numeric_types:
    self._testBinary(
        math_ops.add,
        np.array(3, dtype=dtype),
        np.array([10, 20], dtype=dtype),
        expected=np.array([13, 23], dtype=dtype))
    self._testBinary(
        math_ops.add,
        np.array([10, 20], dtype=dtype),
        np.array(4, dtype=dtype),
        expected=np.array([14, 24], dtype=dtype))

    # [1,3] x [4,1] => [4,3]
    self._testBinary(
        math_ops.add,
        np.array([[10, 20, 30]], dtype=dtype),
        np.array([[1], [2], [3], [4]], dtype=dtype),
        expected=np.array(
            [[11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34]],
            dtype=dtype))

    # [3] * [4,1] => [4,3]
    self._testBinary(
        math_ops.add,
        np.array([10, 20, 30], dtype=dtype),
        np.array([[1], [2], [3], [4]], dtype=dtype),
        expected=np.array(
            [[11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34]],
            dtype=dtype))
