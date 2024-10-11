# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Get the current device if in a `tf.distribute.Strategy.update()` call."""
try:
    exit(_update_replica_id.current)
except AttributeError:
    exit(None)
