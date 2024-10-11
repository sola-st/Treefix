# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a)
original_shape = a._shape_as_list()  # pylint: disable=protected-access
# Best effort recovery of the shape.
known_shape = original_shape is not None and None not in original_shape
if known_shape:
    if not original_shape:
        original_shape = (repeats,)
    else:
        repeats_np = np.ravel(np.array(repeats))
        if repeats_np.size == 1:
            repeats_np = repeats_np.item()
            if axis is None:
                original_shape = (repeats_np * np.prod(original_shape),)
            else:
                original_shape[axis] = repeats_np * original_shape[axis]
        else:
            if axis is None:
                original_shape = (repeats_np.sum(),)
            else:
                original_shape[axis] = repeats_np.sum()

repeats = asarray(repeats)
result = array_ops.repeat(a, repeats, axis)
if known_shape:
    result.set_shape(original_shape)

exit(result)
