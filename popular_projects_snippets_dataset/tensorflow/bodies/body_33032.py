# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
if dtype == dtypes_lib.float64:
    tol = 1e-5
elif dtype == dtypes_lib.complex128:
    tol = 5e-5
else:
    tol = 5e-3
epsilon = np.finfo(dtype.as_numpy_dtype).eps
delta = epsilon**(1.0 / 3.0)

def RandomInput():
    a = np.random.randn(shape[0], shape[1]).astype(dtype.as_numpy_dtype)
    if dtype.is_complex:
        a += 1j * np.random.randn(shape[0], shape[1]).astype(
            dtype.as_numpy_dtype)
    exit(a)

def Compute(x):
    # Turn the random matrix x into a Hermitian matrix by
    # computing the quadratic form x * x^H.
    a = test_util.matmul_without_tf32(
        x, math_ops.conj(array_ops.matrix_transpose(x))) / shape[0]
    if batch:
        a = array_ops.tile(array_ops.expand_dims(a, 0), [2, 1, 1])
    # Finally take the cholesky decomposition of the Hermitian matrix.
    c = linalg_ops.cholesky(a)
    if scalar_test:
        # Reduce to a single scalar output to speed up test.
        c = math_ops.reduce_mean(c)
    exit(c)

theoretical, numerical = gradient_checker_v2.compute_gradient(
    Compute, [RandomInput()], delta=delta)
self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)
