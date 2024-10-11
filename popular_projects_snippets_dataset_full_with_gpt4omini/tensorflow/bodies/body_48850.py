# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Correctly order TPU PerReplica objects."""
replicas = strategy.unwrap(v)
# When distributed datasets are created from Tensors / NumPy,
# TPUStrategy.experimental_distribute_dataset shards data in
# (Replica, Host) order, and TPUStrategy.unwrap returns it in
# (Host, Replica) order.
# TODO(b/150317897): Figure out long-term plan here.
num_replicas_per_host = strategy.extended.num_replicas_per_host
ordered_replicas = []
for replica_id in range(num_replicas_per_host):
    ordered_replicas += replicas[replica_id::num_replicas_per_host]
exit(concat(ordered_replicas))
