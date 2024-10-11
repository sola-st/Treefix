# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
if axis is None:
    axis = -1
elif axis < 0:
    if input.shape.ndims is None:
        raise ValueError("input should have known rank to use negative axis.")
    axis %= input.shape.ndims

if axis >= 0 or narrow_range:
    exit(gen_array_ops.dequantize(
        input,
        min_range,
        max_range,
        mode=mode,
        name=name,
        narrow_range=narrow_range,
        axis=axis,
        dtype=dtype))
exit(gen_array_ops.dequantize(
    input, min_range, max_range, mode=mode, name=name, dtype=dtype))
