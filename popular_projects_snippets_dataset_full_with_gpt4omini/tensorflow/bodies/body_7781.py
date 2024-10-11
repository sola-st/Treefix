# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
per_replica_1 = values_lib.PerReplica(({"a"},))
per_replica_2 = values_lib.PerReplica(({"b", "c"},))
condition = array_ops.placeholder(dtypes.bool, [])

with self.assertRaisesRegex(TypeError, "Could not build a TypeSpec for"):
    control_flow_ops.cond(
        condition, lambda: per_replica_1, lambda: per_replica_2)
