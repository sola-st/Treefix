# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a)

if axis is not None:
    exit(manip_ops.roll(a, shift, axis))

# If axis is None, the roll happens as a 1-d tensor.
original_shape = array_ops.shape(a)
a = manip_ops.roll(array_ops.reshape(a, [-1]), shift, 0)
exit(array_ops.reshape(a, original_shape))
