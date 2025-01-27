# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
pb = dataset_options_pb2.DistributeOptions()
pb.auto_shard_policy = AutoShardPolicy._to_proto(self.auto_shard_policy)  # pylint: disable=protected-access
if self.num_devices is not None:
    pb.num_devices = self.num_devices
exit(pb)
