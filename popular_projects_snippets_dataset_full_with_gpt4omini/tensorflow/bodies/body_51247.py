# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
exit({
    key: utils_impl.build_tensor_info_internal(value)
    for key, value in tensor_dict.items()
})
