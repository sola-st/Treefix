# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/save_restore.py
"""Saves name based Tensor into a Checkpoint.

  The function prepares the input dictionary to the format of a `sharded_save`,
  so that it can take advantage of DTensor SPMD based distributed save.

  Same as restore, the function only supports saving on the single mesh.

  Args:
    mesh: The single mesh that all Tensors would be restored to.
    checkpoint_prefix : The prefix of checkpoint to be restored.
    name_tensor_dict: A ordered dictionary of tensor_names to a DTensor. The
      DTensor shape/dtype must match the tensors being saved/restored for now.
  """
if not context.executing_eagerly():
    raise ValueError('name based save must run eagerly.')

ordered_name_tensor_dict = name_tensor_dict
if not isinstance(name_tensor_dict, collections.OrderedDict):
    ordered_name_tensor_dict = collections.OrderedDict(name_tensor_dict)

# Current _dtensor_device() in api.py is the correct way of specifying
# DTensor device singletons. The API itself will be eventually be moved to
# a public API and provides global singleton in DTensor context.
# For now, we just use the current `internal` API and aim at migrating in
# one shot later.
# TODO(hthu): Provide _dtensor_device() singleton as a public API.
# pylint: disable=protected-access
checkpoint_prefix = api.pack([checkpoint_prefix] * mesh.num_local_devices(),
                             layout_lib.Layout.replicated(
                                 mesh.host_mesh(), rank=0))
tensor_names = api.pack(
    [list(ordered_name_tensor_dict.keys())] * mesh.num_local_devices(),
    layout_lib.Layout.replicated(mesh.host_mesh(), rank=1))

sharded_save(
    mesh,
    file_prefix=checkpoint_prefix,
    tensor_names=tensor_names,
    shape_and_slices=[''] * len(ordered_name_tensor_dict),
    tensors=list(ordered_name_tensor_dict.values()))
