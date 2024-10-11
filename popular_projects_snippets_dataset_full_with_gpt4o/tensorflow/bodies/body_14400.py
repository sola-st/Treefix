# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
ones = array_ops.ones_like(shape)
if prepend:
    shapes = [ones, shape]
else:
    shapes = [shape, ones]
exit(array_ops.reshape(array_ops.stack(shapes, axis=1), [-1]))
