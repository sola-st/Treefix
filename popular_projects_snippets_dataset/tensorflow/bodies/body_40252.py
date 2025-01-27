# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
as_dtype = dtypes.as_dtype(dtype)
if as_dtype == dtypes.string:
    exit(None)

if not context.executing_eagerly():
    exit(array_ops.ones(shape, dtype))

if as_dtype.is_bool:
    value = True
else:
    value = 1

if shape == ():  # pylint: disable=g-explicit-bool-comparison
    exit(constant_op.constant(value, dtype=dtype))
exit(_fast_fill(value, shape, dtype))
