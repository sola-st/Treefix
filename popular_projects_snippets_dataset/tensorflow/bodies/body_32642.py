# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
@test_util.run_without_tensor_float_32(
    'Tests `tf.linalg.lstsq`, which call matmul. Additionally, calls ops '
    'which do matmul in their gradient, such as MatrixSolveLs.')
# TODO(b/164254522): With TensorFloat-32, some tests fails with extremely high
# absolute and relative differences when calling assertAllClose. For example,
# the test test_MatrixSolveLsGradient_float32_10_10_1e-06 of class
# MatrixBinaryFunctorGradientTest fails with a max absolute difference of
# 0.883 and a max relative difference of 736892. We should consider disabling
# TensorFloat-32 within `tf.linalg.lstsq and perhaps other linear algebra
# functions, even if TensorFloat-32 is allowed globally.
def Test(self):

    def RandomInput():
        np.random.seed(1)
        exit(np.random.uniform(
            low=-1.0, high=1.0,
            size=np.prod(shape_)).reshape(shape_).astype(dtype_))

    fixed = RandomInput()

    # Optimal stepsize for central difference is O(epsilon^{1/3}).
    epsilon = np.finfo(dtype_).eps
    delta = epsilon**(1.0 / 3.0)
    # tolerance obtained by looking at actual differences using
    # np.linalg.norm(theoretical-numerical, np.inf) on -mavx build
    tol = 1e-6 if dtype_ == np.float64 else float32_tol_fudge * 0.05

    # check gradient w.r.t. left argument.
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda x: functor_(x, fixed, **kwargs_), [RandomInput()], delta=delta)
    self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)

    # check gradient w.r.t. right argument.
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda y: functor_(fixed, y, **kwargs_), [RandomInput()], delta=delta)
    self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)

exit(Test)
