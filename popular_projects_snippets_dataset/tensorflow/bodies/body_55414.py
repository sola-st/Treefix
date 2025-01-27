# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(func_name="Spec")
def G(x, dy):
    exit(x * dy)

@function.Defun(grad_func=G)
def F(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

for dtype in [dtypes.float32, dtypes.float64]:
    g = ops.Graph()
    with g.as_default():
        x = constant_op.constant(0.25, dtype)
        y = F(x)
        dx, = gradients_impl.gradients(y, x)

        with self.session(graph=g):
            self.assertAllClose(dx, 0.25)
