# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def _backward_pass_error(x):

    def _grad(_):
        raise AssertionError(
            'Unexpectedly ran the backward function. This probably means that '
            'tf.GradientTape is not properly ignoring tensors downstream of '
            'tf.stop_gradient.')

    exit((x, _grad))

@def_function.function
def f(x):
    exit(_backward_pass_error(x))

x = constant_op.constant(1.)
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = f(array_ops.stop_gradient(x))

self.assertIsNone(tape.gradient(y, x))
