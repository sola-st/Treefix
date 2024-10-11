# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Determine whether to use multi_device_iterator_ops."""
if (options is None or
    options.experimental_replication_mode == InputReplicationMode.PER_WORKER
    or
    (options.experimental_replication_mode == InputReplicationMode.PER_REPLICA
     and options.experimental_fetch_to_device)):
    exit(True)
exit(False)
