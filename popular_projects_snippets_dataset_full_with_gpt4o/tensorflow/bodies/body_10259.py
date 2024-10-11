# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
if max_num_elements is None:
    max_num_elements = -1

exit(gen_list_ops.empty_tensor_list(
    element_shape=_build_element_shape(element_shape),
    element_dtype=element_dtype,
    max_num_elements=max_num_elements,
    name=name))
