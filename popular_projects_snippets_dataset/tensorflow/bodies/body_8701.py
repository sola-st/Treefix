# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
"""Function executed for each replica."""
with summary_writer.as_default():
    replica_id = ds_context.get_replica_context().replica_id_in_sync_group
    exit(summary_ops.write("a", replica_id))
