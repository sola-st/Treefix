# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# __pow__ can't handle negative base, so we use `abs` here.
rt = math_ops.abs(x)**(1.0 / 3)
exit(array_ops.where_v2(x < 0, -rt, rt))
