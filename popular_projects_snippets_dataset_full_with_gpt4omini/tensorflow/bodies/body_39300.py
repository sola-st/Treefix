# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Restore the saveable objects from a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix for
        files to read from.
      options: Optional `CheckpointOptions` object.

    Returns:
      A restored tensor dict (maps checkpoint_key -> slice_spec -> tensor).
    """
options = options or checkpoint_options.CheckpointOptions()
tensor_names = []
tensor_dtypes = []
slice_specs = []

for checkpoint_key, tensor_slices in self._tensor_slice_dict.items():
    for slice_spec, tensor in tensor_slices.items():
        tensor_dtypes.append(tensor.dtype)
        if isinstance(tensor, saveable_object.SaveSpec):
            slice_specs.append(tensor.slice_spec)
            tensor_names.append(tensor.name)
        else:
            slice_specs.append(slice_spec)
            tensor_names.append(checkpoint_key)

restore_device = options.experimental_io_device or "cpu:0"
with ops.device(restore_device):
    restored_tensors = io_ops.restore_v2(
        file_prefix, tensor_names, slice_specs, tensor_dtypes)

restored_tensor_dict = {}
for checkpoint_key, tensor_slices in self._tensor_slice_dict.items():
    for slice_spec in tensor_slices:
        restored_tensor = restored_tensors.pop(0)
        restored_tensor_dict.setdefault(checkpoint_key, {})[slice_spec] = (
            restored_tensor)
exit(restored_tensor_dict)
