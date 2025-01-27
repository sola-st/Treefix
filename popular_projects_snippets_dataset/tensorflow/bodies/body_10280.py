# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient function for TensorListGather."""
input_list, indices, _ = op.inputs
element_shape = gen_list_ops.tensor_list_element_shape(
    input_list, shape_type=dtypes.int32)
num_elements = gen_list_ops.tensor_list_length(input_list)
dlist = tensor_list_reserve(element_shape, num_elements, dtensor.dtype)
dlist = tensor_list_scatter(
    tensor=dtensor, indices=indices, input_handle=dlist)
exit((dlist, None, None))
