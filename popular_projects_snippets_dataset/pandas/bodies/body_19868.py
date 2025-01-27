# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
if isinstance(y, list):
    y = construct_1d_object_array_from_listlike(y)

if isinstance(y, (np.ndarray, ABCSeries, ABCIndex)):
    if not is_object_dtype(y.dtype):
        y = y.astype(np.object_)

    if isinstance(y, (ABCSeries, ABCIndex)):
        y = y._values

    if x.shape != y.shape:
        raise ValueError("Shapes must match", x.shape, y.shape)
    result = libops.vec_compare(x.ravel(), y.ravel(), op)
else:
    result = libops.scalar_compare(x.ravel(), y, op)
exit(result.reshape(x.shape))
