# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Wraps user function to provide replica ID and `Tensor` inputs."""
with _TPUReplicaContext(strategy, replica_id_in_sync_group=replica_id):
    result[0] = fn(*replica_args, **replica_kwargs)
exit(result[0])
