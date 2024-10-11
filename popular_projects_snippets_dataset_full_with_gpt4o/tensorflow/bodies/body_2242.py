# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        math_ops.multiply,
        np.array([1, 20], dtype=dtype),
        np.array([10, 2], dtype=dtype),
        expected=np.array([10, 40], dtype=dtype))
    self._testBinary(
        math_ops.multiply,
        dtype(5),
        np.array([1, 20], dtype=dtype),
        expected=np.array([5, 100], dtype=dtype))
    self._testBinary(
        math_ops.multiply,
        np.array([[10], [2]], dtype=dtype),
        dtype(7),
        expected=np.array([[70], [14]], dtype=dtype))

    if dtype not in self.int_types:
        self._testBinary(
            math_ops.multiply,
            np.array([1.9131952969218875, 1.596299504298079], dtype=dtype),
            np.array([1.1137667913355869, 1.7186636469261405], dtype=dtype),
            expected=np.array([2.130853387051026, 2.743501927643327],
                              dtype=dtype),
            rtol=1e-14)
