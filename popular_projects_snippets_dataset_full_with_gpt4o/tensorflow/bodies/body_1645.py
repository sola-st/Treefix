# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py

if xla_test.test.is_built_with_rocm():
    # The folowing subtest invokes the call to "BlasTrsm"
    # That operation is currently not supported on the ROCm platform
    self.skipTest("BlasTrsm op for complex types is not supported in ROCm")

rng = np.random.RandomState(0)
a = np.tril(rng.randn(5, 5) + rng.randn(5, 5) * 1j)
b = rng.randn(5, 7) + rng.randn(5, 7) * 1j
for dtype in self.complex_types:
    self._VerifyTriangularSolveCombo(a.astype(dtype), b.astype(dtype))
