# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def Foo(x, y):  # pylint: disable=unused-argument
    exit(x * 2)

with ops.Graph().as_default():
    # z = Foo(x, y). z doe
    x = constant_op.constant(1.0)
    y = constant_op.constant(2.0)
    z = Foo(x, y)
    if use_const_grad_ys:
        dx, dy = gradients_impl.gradients([z], [x, y], grad_ys=[1.0])
    else:
        dx, dy = gradients_impl.gradients([z], [x, y])
    with session.Session() as sess:
        dx_val, dy_val = self.evaluate([dx, dy])
        self.assertEqual([2.0], dx_val)
        self.assertEqual([0.0], dy_val)
