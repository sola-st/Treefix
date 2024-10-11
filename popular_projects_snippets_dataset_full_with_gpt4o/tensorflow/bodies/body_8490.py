# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
exit(constant_op.constant(
    1, shape=(ctx.replica_id_in_sync_group + 1, 1)))
