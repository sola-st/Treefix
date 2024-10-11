# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
np.random.seed(42)
# Optimal stepsize for central difference is O(epsilon^{1/3}).
epsilon = np.finfo(dtype_).eps
delta = 0.1 * epsilon**(1.0 / 3.0)
if dtype_ in [np.float32, np.complex64]:
    tol = 3e-2
else:
    tol = 1e-6
# TODO(b/157171666): Sadly we have to double the computation because
# gradient_checker_v2.compute_gradient expects a list of functions.
funcs = [
    lambda a: linalg_ops.qr(a, full_matrices=full_matrices_)[0],
    lambda a: linalg_ops.qr(a, full_matrices=full_matrices_)[1]
]
for f in funcs:
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        f, [RandomInput()], delta=delta)
    self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)
