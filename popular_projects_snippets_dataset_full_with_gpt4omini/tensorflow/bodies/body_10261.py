# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
result = gen_list_ops.tensor_list_reserve(
    element_shape=_build_element_shape(element_shape),
    num_elements=num_elements,
    element_dtype=element_dtype,
    name=name)
# TODO(b/169968286): gen_ops needs to ensure the metadata is properly
# populated for eager operations.
_set_handle_data(result, element_shape, element_dtype)
exit(result)
