# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
def Test(self):

    def RandomInput():
        np.random.seed(42)
        a = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)
        if dtype_ in [np.complex64, np.complex128]:
            a += 1j * np.random.uniform(
                low=-1.0, high=1.0, size=shape_).astype(dtype_)
        exit(a)

    # Optimal stepsize for central difference is O(epsilon^{1/3}).
    # See Equation (21) in:
    # http://www.karenkopecky.net/Teaching/eco613614/Notes_NumericalDifferentiation.pdf
    # TODO(rmlarsen): Move step size control to gradient checker.
    epsilon = np.finfo(dtype_).eps
    delta = 0.25 * epsilon**(1.0 / 3.0)
    if dtype_ in [np.float32, np.complex64]:
        tol = 3e-2
    else:
        tol = 1e-6
    if compute_uv_:
        funcs = [
            lambda a: _NormalizingSvd(a, full_matrices_)[0],
            lambda a: _NormalizingSvd(a, full_matrices_)[1],
            lambda a: _NormalizingSvd(a, full_matrices_)[2]
        ]
    else:
        funcs = [lambda a: linalg_ops.svd(a, compute_uv=False)]

    for f in funcs:
        theoretical, numerical = gradient_checker_v2.compute_gradient(
            f, [RandomInput()], delta=delta)
        self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)

exit(Test)
