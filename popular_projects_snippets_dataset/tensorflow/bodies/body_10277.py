# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient for TensorListGetItem."""
list_size = gen_list_ops.tensor_list_length(op.inputs[0])
list_grad = gen_list_ops.tensor_list_set_item(
    gen_list_ops.tensor_list_reserve(
        gen_list_ops.tensor_list_element_shape(op.inputs[0],
                                               shape_type=dtypes.int32),
        list_size, element_dtype=ditem.dtype),
    index=op.inputs[1],
    item=ditem)
index_grad = None
element_shape_grad = None
exit((list_grad, index_grad, element_shape_grad))
