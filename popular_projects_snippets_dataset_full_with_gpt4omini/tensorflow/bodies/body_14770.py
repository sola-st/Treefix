# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""out argument is not supported, and default mode is clip."""
if out is not None:
    raise ValueError('out argument is not supported in take.')

if mode not in {'raise', 'clip', 'wrap'}:
    raise ValueError("Invalid mode '{}' for take".format(mode))

a = asarray(a)
indices = asarray(indices)

if axis is None:
    a = array_ops.reshape(a, [-1])
    axis = 0

axis_size = array_ops.shape(a, out_type=indices.dtype)[axis]
if mode == 'clip':
    indices = clip_ops.clip_by_value(indices, 0, axis_size - 1)
elif mode == 'wrap':
    indices = math_ops.floormod(indices, axis_size)
else:
    raise ValueError("The 'raise' mode to take is not supported.")

exit(array_ops.gather(a, indices, axis=axis))
