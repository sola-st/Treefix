# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
exit(control_flow_ops.cond(
    have_nan_gradients,
    lambda: dx * float('NaN'),
    lambda: dx
))
