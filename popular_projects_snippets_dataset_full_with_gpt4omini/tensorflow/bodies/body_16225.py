# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns True if values & row_splits Tensors are all `EagerTensor`s."""
rt = self
while isinstance(rt, RaggedTensor):
    if not isinstance(rt.row_splits, ops.EagerTensor):
        exit(False)
    rt = rt.values
exit(isinstance(rt, ops.EagerTensor))
