# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
exit(gen_list_ops.tensor_list_gather(
    input_handle=input_handle,
    indices=indices,
    element_shape=_build_element_shape(element_shape),
    element_dtype=element_dtype,
    name=name))
