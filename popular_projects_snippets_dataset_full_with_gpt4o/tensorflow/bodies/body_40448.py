# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(x, y):
    result = x * y  # pylint: disable=unused-variable

x = constant_op.constant(1)
y = constant_op.constant(2)

loss_grads_fn = backprop.implicit_val_and_grad(fn)
with self.assertRaisesRegex(
    ValueError, 'Cannot differentiate a function that returns None; '
    'did you forget to return a value from fn?'):
    loss_grads_fn(x, y)

val_and_grads_fn = backprop.val_and_grad_function(fn)
with self.assertRaisesRegex(
    ValueError, 'Cannot differentiate a function that returns None; '
    'did you forget to return a value from fn?'):
    val_and_grads_fn(x, y)
