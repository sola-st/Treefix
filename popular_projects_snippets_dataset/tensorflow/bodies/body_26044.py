# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
self.auto_shard_policy = AutoShardPolicy._from_proto(pb.auto_shard_policy)  # pylint: disable=protected-access
if pb.WhichOneof("optional_num_devices") is not None:
    self.num_devices = pb.num_devices
