# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
x = ragged_factory_ops.constant(x)
if grad_y is not None:
    grad_y = ragged_factory_ops.constant(grad_y)
if context.executing_eagerly():
    with backprop.GradientTape() as t:
        t.watch(x)
        y = func(x)
    g = t.gradient(y, x, grad_y)
else:
    y = func(x)
    g = gradients_impl.gradients(ys=y, xs=x, grad_ys=grad_y)[0]
if expected_grad is None:
    self.assertIsNone(g)
else:
    g = ragged_tensor.convert_to_tensor_or_ragged_tensor(g)
    self.assertAllClose(g, expected_grad)
