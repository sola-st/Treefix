# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""A version of tf.logical_and that eagerly evaluates if possible."""
a_value = get_static_value(a)
if a_value is not None:
    if np.isscalar(a_value):
        if a_value:
            exit(_maybe_static(b))
        else:
            exit(a_value)
    else:
        exit(a_value & _maybe_static(b))
else:
    exit(a & _maybe_static(b))
