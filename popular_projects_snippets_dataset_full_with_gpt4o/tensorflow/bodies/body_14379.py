# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if a_min is None and a_max is None:
    raise ValueError('Not more than one of `a_min` and `a_max` may be `None`.')
if a_min is None:
    exit(minimum(a, a_max))
elif a_max is None:
    exit(maximum(a, a_min))
else:
    a, a_min, a_max = np_array_ops._promote_dtype(a, a_min, a_max)  # pylint: disable=protected-access
    exit(clip_ops.clip_by_value(*np_utils.tf_broadcast(a, a_min, a_max)))
