# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
"""Test cases for division operators."""
self._testBinary(
    math_ops.div,
    np.array([10, 20], dtype=dtype),
    np.array([10, 2], dtype=dtype),
    expected=np.array([1, 10], dtype=dtype))
self._testBinary(
    math_ops.div,
    dtype(40),
    np.array([2, 20], dtype=dtype),
    expected=np.array([20, 2], dtype=dtype))
self._testBinary(
    math_ops.div,
    np.array([[10], [4]], dtype=dtype),
    dtype(2),
    expected=np.array([[5], [2]], dtype=dtype))

if dtype in [np.float32, np.float64]:
    nums = np.arange(-10, 10, .25, dtype=dtype).reshape(80, 1)
    divs = np.arange(-3, 3, .25, dtype=dtype).reshape(1, 24)
    np_result = np.true_divide(nums, divs)
    np_result[:, divs[0] == 0] = 0
    self._testBinary(
        gen_math_ops.div_no_nan,
        nums,
        divs,
        expected=np_result,
        rtol=7e-15 if dtype == np.float64 else None,
        atol=3.9e-15 if dtype == np.float64 else None)

# floordiv/truncatediv unsupported for complex.
if dtype not in self.complex_types:
    self._testBinary(
        gen_math_ops.floor_div,
        np.array([3, 3, -1, -9, -8], dtype=dtype),
        np.array([2, -2, 7, 2, -4], dtype=dtype),
        expected=np.array([1, -2, -1, -5, 2], dtype=dtype))

    self._testBinary(
        gen_math_ops.truncate_div,
        np.array([3, 3, -1, -9, -8.1], dtype=dtype),
        np.array([2, -2, 7, 2, -4], dtype=dtype),
        expected=np.array([1, -1, 0, -4, 2], dtype=dtype))

if dtype in self.signed_int_types:
    # Overflow cases.
    int_min = np.iinfo(dtype).min
    int_max = np.iinfo(dtype).max
    self._testBinary(
        gen_math_ops.floor_div,
        np.array([int_min, -1, 1, int_max], dtype=dtype).reshape([1, 4]),
        np.array([int_min, -1, 1, int_max], dtype=dtype).reshape([4, 1]),
        expected=np.array([[1, 0, -1, -1], [int_min, 1, -1, -1 * int_max],
                           [int_min, -1, 1, int_max], [-2, -1, 0, 1]],
                          dtype=dtype))
