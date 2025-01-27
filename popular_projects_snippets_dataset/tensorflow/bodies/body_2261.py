# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
self._testMatMul(math_ops.matmul, self.float_types | {np.float64})

for dtype in self.float_types | {np.float64}:
    self._testBinary(
        math_ops.matmul,
        np.array([[3.1415926535897932]], dtype=dtype),
        np.array([[2.7182818284590452]], dtype=dtype),
        expected=np.array([[8.5397342226735668]], dtype=dtype),
        rtol=1e-14)

    # Edge case with a large range of exponent. Not supported by float16.
    if dtype != np.float16:
        self._testBinary(
            math_ops.matmul,
            np.array([[9.4039548065783000e-38]], dtype=dtype),
            np.array([[4.5070591730234615e37]], dtype=dtype),
            expected=np.array([[4.2384180773686798]], dtype=dtype),
            rtol=1e-14)
