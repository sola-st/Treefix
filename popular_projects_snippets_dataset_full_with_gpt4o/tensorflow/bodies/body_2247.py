# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.complex_types:
    ctypes = {np.complex64: np.float32, np.complex128: np.float64}
    self._testBinary(
        math_ops.complex,
        np.array([[[[-1, 2], [2, 0]]]], dtype=ctypes[dtype]),
        np.array([[[[2, -3], [0, 4]]]], dtype=ctypes[dtype]),
        expected=np.array([[[[-1 + 2j, 2 - 3j], [2, 4j]]]], dtype=dtype))

    self._testBinary(
        lambda x, y: math_ops.approximate_equal(x, y, tolerance=0.0001),
        np.array([[[[-1 + 2j, 2.00009999 - 3j], [2 - 3j, 3 + 4.01j]]]],
                 dtype=dtype),
        np.array([[[[-1.001 + 2j, 2 - 3j], [2 - 3.00009j, 3 + 4j]]]],
                 dtype=dtype),
        expected=np.array([[[[False, True], [True, False]]]], dtype=dtype))

    self._testBinary(
        gen_math_ops.real_div,
        np.array(
            [3, 3j, -1.5j, -8, 2 + 3j, 2 + 4j, 9.663546088957395e-28 + 0j],
            dtype=dtype),
        np.array([
            2, -2, 7j, -4j, 4 - 6j, 1 + 2j,
            9.39511792677288e-16 - 1.529841108938729e-23j
        ],
                 dtype=dtype),
        expected=np.array([
            1.5, -1.5j, -0.2142857, -2j,
            (2 + 3j) / (4 - 6j), 2, 1.028571e-12 + 1.674859e-20j
        ],
                          dtype=dtype))

    self._testBinary(
        math_ops.pow,
        dtype(3 + 2j),
        dtype(4 - 5j),
        expected=np.power(dtype(3 + 2j), dtype(4 - 5j)))
    self._testBinary(  # empty rhs
        math_ops.pow,
        np.array([1 + 2j, 2 - 3j], dtype=dtype),
        np.zeros(shape=[0, 2], dtype=dtype),
        expected=np.zeros(shape=[0, 2], dtype=dtype))
    self._testBinary(  # to zero power
        math_ops.pow,
        np.array([1 + 2j, 2 - 3j], dtype=dtype),
        np.zeros(shape=[1, 2], dtype=dtype),
        expected=np.ones(shape=[1, 2], dtype=dtype))
    lhs = np.array([1 - 2j, 4 + 3j, 2 - 3j, 3, 2j, 1, 4], dtype=dtype)
    rhs = np.array([2, 3j, 3 + 4j, 2 + 3j, 3 - 2j, 2, 3 + 3j], dtype=dtype)
    scalar = dtype(2 + 2j)
    self._testBinary(math_ops.pow, lhs, rhs, expected=np.power(lhs, rhs))
    self._testBinary(
        math_ops.pow, scalar, rhs, expected=np.power(scalar, rhs))
    self._testBinary(math_ops.pow, lhs, scalar, np.power(lhs, scalar))

    lhs = np.array([4 + 2j, -3 - 1j, 2j, 1], dtype=dtype)
    rhs = np.array([5, -6j, 7 - 3j, -8j], dtype=dtype)
    self._testBinary(
        gen_math_ops.reciprocal_grad, lhs, rhs, expected=-rhs * lhs * lhs)

    self._testBinary(
        gen_math_ops.sigmoid_grad, lhs, rhs, expected=rhs * lhs * (1 - lhs))

    self._testBinary(
        gen_math_ops.rsqrt_grad, lhs, rhs, expected=lhs**3 * rhs / -2)

    self._testBinary(
        gen_math_ops.sqrt_grad, lhs, rhs, expected=rhs / (2 * lhs))

    self._testBinary(
        gen_math_ops.tanh_grad, lhs, rhs, expected=rhs * (1 - lhs * lhs))
