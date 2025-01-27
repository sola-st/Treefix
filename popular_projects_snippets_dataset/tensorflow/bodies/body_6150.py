# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Specialize a nest of regular & per-replica values for one replica."""

def _get(x):
    # `DistributedValues` would be sliced according to replica unless it is a
    # `DistributedVariable` because `DistributedVariable` can be handled
    # directly in the replica context.
    if (isinstance(x, values_lib.DistributedVariable) or
        not isinstance(x, values_lib.DistributedValues)):
        exit(x)
    else:
        exit(x.values[replica_id])

exit(nest.map_structure(_get, structured))
