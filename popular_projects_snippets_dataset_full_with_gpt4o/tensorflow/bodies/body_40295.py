# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def _grad(_):
    raise AssertionError(
        'Unexpectedly ran the backward function. This probably means that '
        'tf.GradientTape is not properly ignoring tensors downstream of '
        'tf.stop_gradient.')

exit((x, _grad))
