# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Save the saveable objects to a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix to
        save under.
      options: Optional `CheckpointOptions` object.
    Returns:
      An `Operation`, or None when executing eagerly.
    """
options = options or checkpoint_options.CheckpointOptions()
tensor_names = []
tensors = []
slice_specs = []
for checkpoint_key, tensor_slices in self._tensor_slice_dict.items():
    for slice_spec, tensor in tensor_slices.items():
        if isinstance(tensor, saveable_object.SaveSpec):
            tensor_value = tensor.tensor
            # A tensor value of `None` indicates that this SaveableObject gets
            # recorded in the object graph, but that no value is saved in the
            # checkpoint.
            if tensor_value is not None:
                tensor_names.append(tensor.name)
                tensors.append(tensor_value)
                slice_specs.append(tensor.slice_spec)
        else:
            tensor_names.append(checkpoint_key)
            tensors.append(tensor)
            slice_specs.append(slice_spec)
save_device = options.experimental_io_device or (
    len(tensors) and saveable_object_util.set_cpu0(tensors[0].device))
save_device = save_device or "cpu:0"
with ops.device(save_device):
    exit(io_ops.save_v2(file_prefix, tensor_names, slice_specs, tensors))
