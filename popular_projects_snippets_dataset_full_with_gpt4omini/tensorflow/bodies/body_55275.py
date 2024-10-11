# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
dtype = dtypes.float32

@function.Defun(dtype, dtype, dtype)
def Grad(x, dy, dz):
    # Should have returned 1 result.
    exit((x, dy + dz))

@function.Defun(dtype, grad_func=Grad)
def Forward(x):
    exit((x, x))

g = ops.Graph()
with g.as_default():
    inp = array_ops.placeholder(dtype)
    out = math_ops.add_n(Forward(inp))
    dinp = gradients_impl.gradients(out, [inp])

x = np.random.uniform(-10., 10., size=(4, 9)).astype(np.float32)
with session.Session(graph=g) as sess:
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "SymGrad expects to return 1.*but get 2.*instead"):
        _ = sess.run(dinp, {inp: x})
