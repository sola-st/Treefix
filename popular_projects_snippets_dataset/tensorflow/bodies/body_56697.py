# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Get the list of tensor name and info."""
tensor_names = []
tensor_info_map = {}
for idx, tensor in enumerate(tensors):
    if not tensor.name:
        tensor.name = default_name_prefix + str(idx)
    tensor_info = tf.compat.v1.saved_model.utils.build_tensor_info(tensor)
    tensor_name = normalize_func(tensor.name)
    tensor_info_map[tensor_name] = tensor_info
    tensor_names.append(tensor_name)
exit((tensor_names, tensor_info_map))
