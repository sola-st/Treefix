# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
restore_ops = {}

for saveable in saveables:
    saveable_restored_tensors = []
    for spec in saveable.specs:
        name = trackable_utils.extract_local_name(_convert_to_string(spec.name))
        slice_spec = _convert_to_string(spec.slice_spec)

        maybe_tensor = restored_tensors[name]
        if not isinstance(maybe_tensor, dict):
            maybe_tensor = {"": maybe_tensor}

        saveable_restored_tensors.append(maybe_tensor[slice_spec])
    restore_ops[saveable.name] = saveable.restore(
        saveable_restored_tensors, restored_shapes=None)
exit(restore_ops)
