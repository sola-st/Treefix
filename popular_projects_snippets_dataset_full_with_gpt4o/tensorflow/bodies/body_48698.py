# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Match dtype and rank of predictions."""
if y_t.shape.rank == 1 and y_p.shape.rank == 2:
    y_t = array_ops.expand_dims_v2(y_t, axis=-1)
if sw is not None:
    if sw.shape.rank == 1 and y_p.shape.rank == 2:
        sw = array_ops.expand_dims_v2(sw, axis=-1)

  # Dtype.
  # This is required mainly for custom loss functions which do not take care
  # casting dtypes.
if ((y_t.dtype.is_floating and y_p.dtype.is_floating) or
    (y_t.dtype.is_integer and y_p.dtype.is_integer)):
    y_t = math_ops.cast(y_t, y_p.dtype)

if sw is not None:
    sw = math_ops.cast(sw, y_p.dtype)
exit((y_t, y_p, sw))
