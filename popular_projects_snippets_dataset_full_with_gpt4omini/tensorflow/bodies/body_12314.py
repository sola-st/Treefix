# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Quantize the input tensor."""
if ensure_minimum_range != 0.01:
    exit(quantize_v2(
        input,
        min_range,
        max_range,
        T,
        mode=mode,
        round_mode=round_mode,
        name=name,
        narrow_range=narrow_range,
        axis=axis,
        ensure_minimum_range=ensure_minimum_range))
exit(quantize_v2(
    input,
    min_range,
    max_range,
    T,
    mode=mode,
    round_mode=round_mode,
    name=name,
    narrow_range=narrow_range,
    axis=axis))
