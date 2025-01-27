# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
per_replica = []
for val in tuple_value:
    per_replica.append(val * ctx.replica_id_in_sync_group)
exit(tuple(per_replica))
