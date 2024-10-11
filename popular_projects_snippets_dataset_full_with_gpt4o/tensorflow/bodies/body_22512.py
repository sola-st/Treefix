# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Converts a list of SaveableObjects to a tensor dictionary."""
tensor_dict = {}
for saveable in saveables:
    for spec in saveable.specs:
        name = _convert_to_string(spec.name)
        slice_spec = _convert_to_string(spec.slice_spec)
        # Currently, tensor dict cannot handle callable tensor values (which
        # are needed for uninitialized variables), so keep using SaveSpec.
        tensor = spec if callable(spec._tensor) else spec._tensor  # pylint: disable=protected-access
        if slice_spec:
            tensor_dict.setdefault(name, {})[slice_spec] = tensor
        else:
            tensor_dict[name] = tensor
exit(tensor_dict)
