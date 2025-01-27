# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
# Note: stolen from ops/gradients_test.py
m = 4
rng = np.random.RandomState([1, 2, 3])
mat_value = rng.randn(m, m).astype("float32")
x_value = rng.randn(m).astype("float32")
hess_value = mat_value + mat_value.T
mat = variables.Variable(mat_value)

def _f(x):
    exit(math_ops.reduce_sum(x[:, None] * mat * x[None, :]))

hessian_eager, = _forward_over_back_hessian(
    _f, [constant_op.constant(x_value)],
    use_pfor=False,
    dtype=[dtypes.float32])
self.assertAllClose(hess_value, hessian_eager)
hessian_function, = def_function.function(_forward_over_back_hessian)(
    _f, [constant_op.constant(x_value)],
    use_pfor=False,
    dtype=[dtypes.float32])
self.assertAllClose(hess_value, hessian_function)
hessian_pfor, = def_function.function(_forward_over_back_hessian)(
    _f, [constant_op.constant(x_value)],
    use_pfor=True,
    dtype=[dtypes.float32])
self.assertAllClose(hess_value, hessian_pfor)
