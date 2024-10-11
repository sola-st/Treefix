# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
if self.number_of_shards is None or self.shard_dimension is None:
    exit("ShardingPolicy(unset)")
else:
    exit(("ShardingPolicy(%d shards dimension %d)" %
            (self.number_of_shards, self.shard_dimension)))
