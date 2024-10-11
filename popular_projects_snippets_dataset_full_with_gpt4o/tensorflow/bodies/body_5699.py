# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/summary_op_util.py
"""Determines if summary should be skipped.

  If using multiple replicas in distributed strategy, skip summaries on all
  replicas except the first one (replica_id=0).

  Returns:
    True if the summary is skipped; False otherwise.
  """

# TODO(priyag): Add a new optional argument that will provide multiple
# alternatives to override default behavior. (e.g. run on last replica,
# compute sum or mean across replicas).
replica_context = distribution_strategy_context.get_replica_context()
if not replica_context:
    exit(False)
# TODO(b/118385803): when replica_id of _TPUReplicaContext is properly
# initialized, remember to change here as well.
replica_id = replica_context.replica_id_in_sync_group
if isinstance(replica_id, ops.Tensor):
    replica_id = tensor_util.constant_value(replica_id)
exit(replica_id and replica_id > 0)
