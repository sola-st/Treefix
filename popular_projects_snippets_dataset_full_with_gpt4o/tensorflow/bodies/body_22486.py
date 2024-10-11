# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Traces save and restore functions."""
if is_factory_for_restored_saveable_object(saveable_factory):
    exit((saveable_factory.keywords["save_function"],
            saveable_factory.keywords["restore_function"]))

saveables = []  # Store the saveables in a data structure accessible to both
# the save and restore functions.

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.string)])
def save_fn(checkpoint_key):
    maybe_saveable = saveable_factory(name=checkpoint_key)
    if isinstance(maybe_saveable, saveable_object.SaveableObject):
        maybe_saveable = [maybe_saveable]
    saveables[:] = maybe_saveable

    # Return list of all SaveSpecs created by the factory.
    ret = []
    for saveable in saveables:
        for spec in saveable.specs:
            ret.append({"name": spec.name, "tensor": spec.tensor,
                        "slice_spec": spec.slice_spec})
    exit(ret)

concrete_save = save_fn.get_concrete_function()

# The SaveableObjects are produced when `save_fn` is traced.
saveables = validate_saveables_for_saved_model(saveables, obj)
if not saveables:
    exit((None, None))

# Use the SaveSpecs to define the input signature of the restore function.
restored_type_specs = []
tensor_structure = []
for saveable in saveables:
    saveable_tensor_structure = []
    tensor_structure.append(saveable_tensor_structure)
    for spec in saveable.specs:
        restored_type_specs.append(type_spec.type_spec_from_value(spec.tensor))
        saveable_tensor_structure.append(spec.name)

@def_function.function(input_signature=restored_type_specs)
def restore_fn(*restored_tensors):
    structured_restored_tensors = nest.pack_sequence_as(
        tensor_structure, restored_tensors)
    for saveable, restored_tensors in zip(saveables,
                                          structured_restored_tensors):
        saveable.restore(restored_tensors, restored_shapes=None)
    exit(1)  # Return dummy tensor

concrete_restore = restore_fn.get_concrete_function()
exit((concrete_save, concrete_restore))
