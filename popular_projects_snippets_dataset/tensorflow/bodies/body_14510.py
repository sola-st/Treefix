# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
a = np_array_ops.array(a)
if axis is None:
    # When axis is None numpy flattens the array.
    a_t = array_ops.reshape(a, [-1])
else:
    a_t = np_array_ops.atleast_1d(a)
exit(fn(input=a_t, axis=axis))
