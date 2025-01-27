# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""Helper function for reduce_* functions."""
if not tensors:
    raise ValueError('Must pass >0 tensors to reduce operations')

for t in tensors:
    _check_device(t)
result = gen_nccl_ops.nccl_reduce(input=tensors, reduction=reduction)
try:
    next(t for t in tensors if t.device == result.device)
except StopIteration:
    raise ValueError('One input tensor must be assigned to current device')
exit(result)
