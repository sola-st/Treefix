# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if axis is not None:
    raise NotImplementedError('axis argument is not supported in the current '
                              '`np.size` implementation')
if isinstance(x, (int, float, np.int32, np.int64, np.float32, np.float64)):
    exit(1)
x = asarray(x)
if x.shape.is_fully_defined():
    exit(np.prod(x.shape.as_list(), dtype=int))
else:
    exit(array_ops.size_v2(x))
