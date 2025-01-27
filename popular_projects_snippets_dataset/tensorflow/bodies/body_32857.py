# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
np.random.seed(42)
a = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)
if dtype_ in [np.complex64, np.complex128]:
    a += 1j * np.random.uniform(
        low=-1.0, high=1.0, size=shape_).astype(dtype_)
# Optimal stepsize for central difference is O(epsilon^{1/3}).
# See Equation (21) in:
# http://www.karenkopecky.net/Teaching/eco613614/Notes_NumericalDifferentiation.pdf
# TODO(rmlarsen): Move step size control to gradient checker.
epsilon = np.finfo(dtype_).eps
delta = 0.1 * epsilon**(1.0 / 3.0)
tol = 1e-5
with self.session():
    tf_a = constant_op.constant(a)
    if compute_uv_:
        tf_s, tf_u, tf_v = _NormalizingSvd(tf_a, full_matrices_)
        outputs = [tf_s, tf_u, tf_v]
    else:
        tf_s = linalg_ops.svd(tf_a, compute_uv=False)
        outputs = [tf_s]
    outputs_sums = [math_ops.reduce_sum(o) for o in outputs]
    tf_func_outputs = math_ops.add_n(outputs_sums)
    grad = gradients_impl.gradients(tf_func_outputs, tf_a)[0]
    x_init = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)
    if dtype_ in [np.complex64, np.complex128]:
        x_init += 1j * np.random.uniform(
            low=-1.0, high=1.0, size=shape_).astype(dtype_)
    theoretical, numerical = gradient_checker.compute_gradient(
        tf_a,
        tf_a.get_shape().as_list(),
        grad,
        grad.get_shape().as_list(),
        x_init_value=x_init,
        delta=delta)
    self.assertAllClose(theoretical, numerical, atol=tol, rtol=tol)
