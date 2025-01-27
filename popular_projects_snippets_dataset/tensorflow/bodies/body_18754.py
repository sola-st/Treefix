# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
rctx = ds_context.get_replica_context()
if rctx is None:
    exit(None)
exit(rctx.replica_id_in_sync_group)
