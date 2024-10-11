# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
"""Get (self.u, self.v) as tensors (in case they were refs)."""
u = ops.convert_to_tensor_v2_with_dispatch(self.u)
if self.v is self.u:
    v = u
else:
    v = ops.convert_to_tensor_v2_with_dispatch(self.v)
exit((u, v))
