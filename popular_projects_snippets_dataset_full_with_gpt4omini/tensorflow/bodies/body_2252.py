# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
"""Test cases for remainder operators."""
self._testBinary(
    gen_math_ops.floor_mod,
    np.array([3, 3, -1, -8], dtype=dtype),
    np.array([2, -2, 7, -4], dtype=dtype),
    expected=np.array([1, -1, 6, 0], dtype=dtype))
self._testBinary(
    gen_math_ops.truncate_mod,
    np.array([3, 3, -1, -8], dtype=dtype),
    np.array([2, -2, 7, -4], dtype=dtype),
    expected=np.array([1, 1, -1, 0], dtype=dtype))
if dtype in self.signed_int_types:
    # Overflow cases.
    int_min = np.iinfo(dtype).min
    int_max = np.iinfo(dtype).max
    self._testBinary(
        gen_math_ops.floor_mod,
        np.array([int_min, -1, 1, int_max], dtype=dtype).reshape([1, 4]),
        np.array([int_min, -1, 1, int_max], dtype=dtype).reshape([4, 1]),
        expected=np.array([[0, -1, -1 * int_max, -1], [0, 0, 0, 0],
                           [0, 0, 0, 0], [int_max - 1, int_max - 1, 1, 0]],
                          dtype=dtype))
    self._testBinary(
        gen_math_ops.truncate_mod,
        np.array([int_min, -1, 1, int_max], dtype=dtype).reshape([1, 4]),
        np.array([int_min, -1, 1, int_max], dtype=dtype).reshape([4, 1]),
        expected=np.array(
            [[0, -1, 1, int_max], [0, 0, 0, 0], [0, 0, 0, 0], [-1, -1, 1, 0]],
            dtype=dtype))
