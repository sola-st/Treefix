# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
per_replica_1 = values_lib.PerReplica(("a",))
per_replica_2 = values_lib.PerReplica(("b",))
condition = array_ops.placeholder_with_default(True, [])

result = control_flow_ops.cond(
    condition, lambda: per_replica_1, lambda: per_replica_2)

self.assertLen(result.values, 1)
self.assertAllEqual(result.values[0], "a")
