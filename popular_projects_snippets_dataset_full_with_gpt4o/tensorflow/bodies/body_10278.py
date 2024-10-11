# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient function for TensorListSetItem."""
_, index, item = op.inputs
list_grad = gen_list_ops.tensor_list_set_item(
    dlist, index=index, item=array_ops.zeros_like(item))
index_grad = None
element_grad = tensor_list_get_item(
    dlist,
    index,
    element_shape=array_ops.shape(item),
    element_dtype=item.dtype)
exit((list_grad, index_grad, element_grad))
