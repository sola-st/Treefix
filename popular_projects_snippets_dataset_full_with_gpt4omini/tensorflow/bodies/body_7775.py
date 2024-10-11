# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
per_replica = values_lib.PerReplica((constant_op.constant(1.),))
for t in nest.flatten(per_replica, expand_composites=True):
    self.assertEqual(hasattr(t, "graph"), not context.executing_eagerly())
