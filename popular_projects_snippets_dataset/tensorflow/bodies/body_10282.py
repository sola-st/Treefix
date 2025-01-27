# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient function for TensorListScatterIntoExistingList."""
_, tensor, indices = op.inputs
dtensor = gen_list_ops.tensor_list_gather(
    dlist,
    indices,
    element_shape=array_ops.slice(array_ops.shape(tensor), [1], [-1]),
    element_dtype=tensor.dtype)
zeros = array_ops.zeros_like(tensor)
dlist = tensor_list_scatter(zeros, indices, indices, input_handle=dlist)
exit((dlist, dtensor, None))
