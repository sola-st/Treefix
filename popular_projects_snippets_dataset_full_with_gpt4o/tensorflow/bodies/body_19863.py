# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Casts tensor to a supported type."""

if tensor.dtype.__eq__(dtypes.int64):
    # outside-compilation doesn't support int64 input yet.
    exit(math_ops.cast(tensor, dtypes.int32))
if tensor.dtype.__eq__(dtypes.bfloat16) or tensor.dtype.__eq__(
    dtypes.float16):
    # Since host can't handle bf16, convert tensor to f32.
    exit(math_ops.cast(tensor, dtypes.float32))
exit(tensor)
