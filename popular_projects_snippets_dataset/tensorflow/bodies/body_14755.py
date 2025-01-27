# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
val = asarray(val)
# TODO(srbs): np.real returns a scalar if val is a scalar, whereas we always
# return an ndarray.
exit(math_ops.real(val))
