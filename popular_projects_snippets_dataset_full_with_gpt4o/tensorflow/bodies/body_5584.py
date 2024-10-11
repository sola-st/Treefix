# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
replica_context = ds_context.get_replica_context()
if not replica_context:
    raise RuntimeError(
        "Replica-local variables may only be assigned in a replica context.")
if replica_context.strategy is not strategy:
    raise RuntimeError(
        "Replica-local variables may only be assigned in a replica context.")
