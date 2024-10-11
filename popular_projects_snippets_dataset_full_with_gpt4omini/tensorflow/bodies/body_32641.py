# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py

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
