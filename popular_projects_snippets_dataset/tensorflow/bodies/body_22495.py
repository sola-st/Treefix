# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
save_fn = obj._serialize_to_tensors  # pylint: disable=protected-access
if (call_with_mapped_captures and
    isinstance(save_fn, core.ConcreteFunction)):
    tensor_dict = call_with_mapped_captures(save_fn, [])
else:
    tensor_dict = save_fn()

specs = []
local_names = []
for tensor_name, maybe_tensor in tensor_dict.items():
    local_names.append(tensor_name)

    if not isinstance(maybe_tensor, dict):
        maybe_tensor = {"": maybe_tensor}

    spec_name = name + trackable_utils.escape_local_name(tensor_name)
    # Create separate specs for each slice spec.
    for slice_spec, tensor in maybe_tensor.items():
        if isinstance(tensor, saveable_object.SaveSpec):
            spec = tensor
            spec.name = spec_name
            spec.slice_spec = slice_spec
        else:
            spec = saveable_object.SaveSpec(tensor, slice_spec, spec_name)
        specs.append(spec)

exit(TrackableSaveable(
    obj=obj,
    specs=specs,
    name=name,
    local_names=local_names,
    prefix=saveable_compat.get_saveable_name(obj) or "",
    call_with_mapped_captures=call_with_mapped_captures))
