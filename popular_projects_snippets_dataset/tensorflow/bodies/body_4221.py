# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/save_restore.py
"""Saves given named tensor slices in a sharded, multi-client safe fashion.

  The method makes sure the checkpoint directory state is correct in a sharded
  mutli-client saving. Namely, we place a barrier after SaveV2 to make sure
  every client has done writing the files. And another one after
  MergeV2Checkpoints to make sure all Metadata is properly merged.

  Upon existing, the checkpoint is completed and the all directory operations
  are done.

  Args:
    mesh: The Mesh that contains the Tensors to save.
    file_prefix: The prefix of checkpoint.
    tensor_names: a list of tensor names used in save op.
    shape_and_slices: a list of shape and slice specification used in save op.
      The only supported value is "" as we don't support distributed saving with
      slices yet.
    tensors: a list of tensors used in save op. The order should match
      tensor_names.

  Returns:
    A MergeV2Checkpoints op that merged all Metadata.
  """
with ops.device(api.device_name()):
    io_ops.save_v2(file_prefix, tensor_names, shape_and_slices, tensors)

# Make sure all clients have written the files
mesh_util.barrier(mesh.host_mesh(), 'SaveV2')  # pylint: disable=protected-access

with api.run_on(mesh.host_mesh()):
    merge_op = io_ops.MergeV2Checkpoints(
        checkpoint_prefixes=[file_prefix],
        destination_prefix=file_prefix,
        delete_old_dirs=True)

# Make sure first device in first host has finished merge.
mesh_util.barrier(mesh.host_mesh(), 'MergeV2Checkpoints')

exit(merge_op)
