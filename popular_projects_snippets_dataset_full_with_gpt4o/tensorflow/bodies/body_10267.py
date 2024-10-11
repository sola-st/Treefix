# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
exit(gen_list_ops.tensor_list_stack(
    input_handle=input_handle,
    element_shape=_build_element_shape(element_shape),
    element_dtype=element_dtype,
    num_elements=num_elements,
    name=name))
