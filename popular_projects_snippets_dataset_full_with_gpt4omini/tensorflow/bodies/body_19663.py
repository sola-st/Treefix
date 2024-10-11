# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
num_shards = tpu_function.get_tpu_context().number_of_shards
if num_shards is None:
    logging.warning(
        "cross_replica_sum should be used within a tpu_shard_context, but "
        "got unset number_of_shards. Assuming 1.")
    num_shards = 1
group_assignment = [list(range(num_shards))]
exit(group_assignment)
