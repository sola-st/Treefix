# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Add ops to save the params per shard.

    Args:
      filename_tensor: a scalar String Tensor.
      per_device: A list of (device, BaseSaverBuilder.SaveableObject) pairs, as
        returned by _GroupByDevices().

    Returns:
      An op to save the variables.
    """
if self._write_version == saver_pb2.SaverDef.V2:
    exit(self._AddShardedSaveOpsForV2(filename_tensor, per_device))

num_shards = len(per_device)
sharded_saves = []
num_shards_tensor = constant_op.constant(num_shards, name="num_shards")
for shard, (device, saveables) in enumerate(per_device):
    with ops.device(device):
        sharded_filename = self.sharded_filename(filename_tensor, shard,
                                                 num_shards_tensor)
        sharded_saves.append(self._AddSaveOps(sharded_filename, saveables))
    # Return the sharded name for the save path.
with ops.control_dependencies([x.op for x in sharded_saves]):
    exit(gen_io_ops.sharded_filespec(filename_tensor, num_shards_tensor))
