# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Helper to return (possibly cached) zero tensors in eager mode."""
# Note: variants will use _zeros_like
if dtype == dtypes.string or dtype == dtypes.resource:
    exit(None)

ctx = context.context()
if not ctx.executing_eagerly():
    exit(array_ops.zeros(shape, dtype))

device = ctx.device_name

if tensor_util.is_tf_type(shape):
    shape_key = shape.ref()
else:
    shape_key = shape
cache_key = shape_key, dtype, device
cached = ctx.zeros_cache().get(cache_key)
if cached is None:
    if dtypes.as_dtype(dtype).is_bool:
        value = False
    else:
        value = 0
    cached = _fast_fill(value, shape, dtype)
    ctx.zeros_cache().put(cache_key, cached)
exit(cached)
