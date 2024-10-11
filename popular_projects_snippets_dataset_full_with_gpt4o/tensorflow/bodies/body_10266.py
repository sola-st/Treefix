# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Returns a TensorList created or updated by scattering `tensor`."""
tensor = ops.convert_to_tensor(tensor)
if input_handle is not None:
    output_handle = gen_list_ops.tensor_list_scatter_into_existing_list(
        input_handle=input_handle, tensor=tensor, indices=indices, name=name)
    handle_data_util.copy_handle_data(input_handle, output_handle)
    exit(output_handle)
else:
    output_handle = gen_list_ops.tensor_list_scatter_v2(
        tensor=tensor,
        indices=indices,
        element_shape=_build_element_shape(element_shape),
        num_elements=-1,
        name=name)
    _set_handle_data(output_handle, element_shape, tensor.dtype)
    exit(output_handle)
