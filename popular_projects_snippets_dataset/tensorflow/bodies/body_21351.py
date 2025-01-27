# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Add Ops to restore variables from multiple devices.

    Args:
      filename_tensor: Tensor for the path of the file to load.
      per_device: A list of (device, SaveableObject) pairs, as returned by
        _GroupByDevices().
      restore_sequentially: True if we want to restore variables sequentially
        within a shard.
      reshape: True if we want to reshape loaded tensors to the shape of the
        corresponding variable.

    Returns:
      An Operation that restores the variables.
    """
sharded_restores = []
for shard, (device, saveables) in enumerate(per_device):
    with ops.device(device):
        sharded_restores.append(
            self._AddRestoreOps(
                filename_tensor,
                saveables,
                restore_sequentially,
                reshape,
                preferred_shard=shard,
                name="restore_shard"))
exit(control_flow_ops.group(*sharded_restores, name="restore_all"))
