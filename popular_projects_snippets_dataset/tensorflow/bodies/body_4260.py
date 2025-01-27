# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
"""Restore the saveable objects from a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix for
        files to read from.
      options: Optional `CheckpointOptions` object. This is unused in DTensor.

    Returns:
      A dictionary mapping from SaveableObject names to restore operations.
    """
if options is not None and options.experimental_io_device is not None:
    raise ValueError(
        "Specified experimental_io_device in DTensor checkpoint is not "
        "supported.")
del options
restore_specs = []
tensor_structure = []
for saveable in self._saveable_objects:
    saveable_tensor_structure = []
    tensor_structure.append(saveable_tensor_structure)
    # DTensor change 1 : Gather shapes and layout from original saveable
    # specs.
    # Note that this relies on the fact that the variables are already
    # initialized -- which isn't the behavior we want eventually.
    # TODO(b/159035705): Handle the variable initialization in restore.
    for spec in saveable.specs:
        saveable_tensor_structure.append(spec.name)
        if isinstance(spec, d_variable.DSaveSpec):
            restore_specs.append((spec.name, spec.slice_spec, spec.dtype,
                                  spec.layout, spec.global_shape))
        # Fall back to replicated layouts for non-DTensor saves that constructs
        # normal SaveSpec.
        elif isinstance(spec, saveable_object.SaveSpec):
            restore_specs.append(
                (spec.name, spec.slice_spec, spec.dtype,
                 layout.Layout.replicated(self._mesh.host_mesh(),
                                          spec.tensor.shape.rank).to_string(),
                 spec.tensor.shape.as_list()))
tensor_names, tensor_slices, tensor_dtypes, layouts, global_shapes = zip(
    *restore_specs)
with ops.device(api.device_name()):
    # DTensor change 2 : Run on customized DTensor RestoreV2 op rather than
    # stock TF io_ops.RestoreV2.
    restored_tensors = gen_dtensor_ops.d_tensor_restore_v2(
        prefix=file_prefix,
        tensor_names=tensor_names,
        shape_and_slices=tensor_slices,
        input_shapes=global_shapes,
        input_layouts=layouts,
        dtypes=tensor_dtypes)
structured_restored_tensors = nest.pack_sequence_as(tensor_structure,
                                                    restored_tensors)
restore_ops = {}
for saveable, restored_tensors in zip(self._saveable_objects,
                                      structured_restored_tensors):
    restore_ops[saveable.name] = saveable.restore(
        restored_tensors, restored_shapes=None)
exit(restore_ops)
