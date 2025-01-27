# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
def Test(self):
    n = shape_[-1]

    np.random.seed(1)
    # Make sure invertible.
    a_np = np.random.uniform(low=1.0, high=2.0, size=shape_).astype(dtype_)
    a = constant_op.constant(a_np)

    b_np = np.random.uniform(low=-1.0, high=1.0, size=[n, n]).astype(dtype_)
    b = constant_op.constant(b_np)

    epsilon = np.finfo(dtype_).eps
    delta = epsilon**(1.0 / 3.0)
    # tolerance obtained by looking at actual differences using
    # np.linalg.norm(theoretical-numerical, np.inf) on -mavx build
    tol = 1e-6 if dtype_ == np.float64 else float32_tol_fudge * 0.05

    # check gradient w.r.t. left argument.
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda x: functor_(x, b, **kwargs_), [a], delta=delta)
    self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)

    # check gradient w.r.t. right argument.
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda y: functor_(a, y, **kwargs_), [b], delta=delta)
    self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)

exit(Test)
