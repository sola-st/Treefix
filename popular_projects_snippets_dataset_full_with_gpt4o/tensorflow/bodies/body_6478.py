# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
cluster_resolver = strategy.cluster_resolver
replica_ctx = ds_context.get_replica_context()
if ((cluster_resolver and cluster_resolver.task_type == "worker") or
    math_ops.equal(replica_ctx.replica_id_in_sync_group,
                   constant_op.constant(1))):
    v_on_read.assign(3.)  # pylint:disable=cell-var-from-loop
else:
    v_on_read.assign(4.)  # pylint:disable=cell-var-from-loop
