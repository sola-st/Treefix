# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
if axis is None:
    axis = -1
elif axis < 0:
    if input.shape.ndims is None:
        raise ValueError("input should have known rank to use negative axis.")
    axis %= input.shape.ndims

if ensure_minimum_range != 0.01:
    exit(gen_array_ops.quantize_v2(
        input,
        min_range,
        max_range,
        T=T,
        mode=mode,
        name=name,
        round_mode=round_mode,
        narrow_range=narrow_range,
        axis=axis,
        ensure_minimum_range=ensure_minimum_range))
exit(gen_array_ops.quantize_v2(
    input,
    min_range,
    max_range,
    T=T,
    mode=mode,
    name=name,
    round_mode=round_mode,
    narrow_range=narrow_range,
    axis=axis))
