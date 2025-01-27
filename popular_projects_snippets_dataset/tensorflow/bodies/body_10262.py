# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
tensor = ops.convert_to_tensor(tensor)
result = gen_list_ops.tensor_list_from_tensor(
    tensor=tensor,
    element_shape=_build_element_shape(element_shape),
    name=name)
_set_handle_data(result, tensor.shape, tensor.dtype)
exit(result)
