# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient function for TensorListScatter."""
tensor = op.inputs[0]
indices = op.inputs[1]
dtensor = gen_list_ops.tensor_list_gather(
    dlist,
    indices,
    element_shape=array_ops.slice(array_ops.shape(tensor), [1], [-1]),
    element_dtype=tensor.dtype)
if op.type == "TensorListScatterV2":
    exit((dtensor, None, None, None))
else:
    exit((dtensor, None, None))
