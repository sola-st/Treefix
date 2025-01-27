# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
# `DistributedValues` would be sliced according to replica unless it is a
# `DistributedVariable` because `DistributedVariable` can be handled
# directly in the replica context.
if (isinstance(x, values_lib.DistributedVariable) or
    not isinstance(x, values_lib.DistributedValues)):
    exit(x)
else:
    exit(x.values[replica_id])
