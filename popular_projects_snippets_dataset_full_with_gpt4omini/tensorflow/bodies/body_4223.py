# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/save_restore.py
"""Restores from checkpoint_prefix to name based DTensors.

  It is required to have already-initialized DTensor variables that have same
  shape/dtype for the tensors being restored.

  Also, we currently only support a named based restore on a single mesh.

  Args:
    mesh: The single mesh that all Tensors would be restored to.
    checkpoint_prefix : The prefix of checkpoint to be restored.
    name_tensor_dict: A ordered dictionary of tensor_names to a DTensor. The
      DTensor shape/dtype must match the tensors being saved/restored for now.

  Returns:
    A dictionary of name to its restored DTensor value.
  """
if not context.executing_eagerly():
    raise ValueError('name based restore must run eagerly.')

ordered_name_tensor_dict = name_tensor_dict
if not isinstance(name_tensor_dict, collections.OrderedDict):
    ordered_name_tensor_dict = collections.OrderedDict(name_tensor_dict)

# Make sure that all tensors are on CPU mesh for now.
# This might not be a hard limitation in the future.
for name, tensor in ordered_name_tensor_dict.items():
    try:
        if api.fetch_layout(tensor).mesh.device_type().upper() != 'CPU':
            raise ValueError(
                'Restoring a non CPU Tensor is not supported currently. Offending '
                'tensor name : {tensor_name}'.format(tensor_name=name))
    except errors_impl.OpError as op_error:
        raise ValueError(
            'Saving/Restoring tensor must be a DTensor') from op_error

  # Now that we have all tensors on CPU mesh, do a DTensorRestoreV2.
checkpoint_prefix = api.pack(
    [checkpoint_prefix] * mesh.num_local_devices(),
    layout_lib.Layout.replicated(mesh.host_mesh(), rank=0))
# Explicitly pack to mesh to avoid implicit small constant extraction, which
# does not work larger restores that has lots of names.
tensor_names = api.pack(
    [list(ordered_name_tensor_dict.keys())] * mesh.num_local_devices(),
    layout_lib.Layout.replicated(mesh.host_mesh(), rank=1))
shape_and_slices = api.pack(
    [[''] * len(ordered_name_tensor_dict)] * mesh.num_local_devices(),
    layout_lib.Layout.replicated(mesh.host_mesh(), rank=1))
# A list of TensorShape representing all shapes for the input tensors.
input_shapes = [tensor.shape for tensor in ordered_name_tensor_dict.values()]
input_layouts = [
    api.fetch_layout(tensor).to_string()
    for tensor in ordered_name_tensor_dict.values()
]

with ops.device(api.device_name()):
    restored_cpu_tensors = gen_dtensor_ops.d_tensor_restore_v2(
        prefix=checkpoint_prefix,
        tensor_names=tensor_names,
        shape_and_slices=shape_and_slices,
        input_shapes=input_shapes,
        input_layouts=input_layouts,
        dtypes=[tensor.dtype for tensor in ordered_name_tensor_dict.values()])

exit(collections.OrderedDict(
    zip(ordered_name_tensor_dict.keys(), restored_cpu_tensors)))
