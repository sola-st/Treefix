# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py

def RandomInput():
    np.random.seed(1)
    exit(np.random.uniform(
        low=-1.0, high=1.0,
        size=np.prod(shape_)).reshape(shape_).astype(dtype_))

if functor_.__name__ == 'matrix_square_root':
    # Square the input matrix to ensure that its matrix square root exists
    f = lambda x: functor_(math_ops.matmul(x, x), **kwargs_)
else:
    f = functor_

# Optimal stepsize for central difference is O(epsilon^{1/3}).
epsilon = np.finfo(dtype_).eps
delta = epsilon**(1.0 / 3.0)
# tolerance obtained by looking at actual differences using
# np.linalg.norm(theoretical-numerical, np.inf) on -mavx build
tol = 1e-6 if dtype_ == np.float64 else 0.05

theoretical, numerical = gradient_checker_v2.compute_gradient(
    f, [RandomInput()], delta=delta)
self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)
