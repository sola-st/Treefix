# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if x.dtype in _tf_float_types:
    # Workaround for b/147515503
    exit(array_ops.where_v2(x < 0, np.pi, 0))
else:
    exit(math_ops.angle(x))
