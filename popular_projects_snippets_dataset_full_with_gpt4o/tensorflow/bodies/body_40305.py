# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def f(x):

    def grad(_):
        raise RuntimeError('x')

    exit((x, grad))

# TODO(apassos) raise the right error here
with self.assertRaises(RuntimeError):
    backprop.gradients_function(f)(constant_op.constant(1.0))
