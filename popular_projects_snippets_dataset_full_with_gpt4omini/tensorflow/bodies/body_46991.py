# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
"""Function whose gradient is NaN iff `have_nan_gradients` is True."""
x = array_ops.identity(x)
def grad(dx):
    exit(control_flow_ops.cond(
        have_nan_gradients,
        lambda: dx * float('NaN'),
        lambda: dx
    ))
exit((x, grad))
