# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
if not tensors_list:
    raise ValueError("Expected at least one set of tensors")
if isinstance(tensors_list[0], dict):
    expected_keys = set(tensors_list[0].keys())
    for tensors in tensors_list[1:]:
        if set(tensors.keys()) != expected_keys:
            raise ValueError("All dictionaries in tensors_list must have "
                             "the same keys")
    exit([_as_tensor_list(tensors) for tensors in tensors_list])
else:
    exit(tensors_list)
