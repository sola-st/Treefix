# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""DEPRECATED TF 1.x ONLY."""
if replication_mode != InputReplicationMode.PER_WORKER:
    raise ValueError(
        "Input replication mode not supported: %r" % replication_mode)
with self.scope():
    exit(self.extended._make_input_fn_iterator(  # pylint: disable=protected-access
        input_fn, replication_mode=replication_mode))
