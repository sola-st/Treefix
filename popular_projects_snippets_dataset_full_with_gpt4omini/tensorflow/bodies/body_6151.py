# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Specialize a nest of regular & mirrored values for one replica."""
assert_mirrored(structured)
exit(select_replica(replica_id, structured))
