# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""A version of tf.cond that tries to evaluate the condition."""
v = get_static_value(pred)
if v is None:
    exit(control_flow_ops.cond(pred, true_fn, false_fn))
if v:
    exit(true_fn())
else:
    exit(false_fn())
