# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
vals = (constant_op.constant(1.), constant_op.constant([5., 6.0]),)
per_replica = values_lib.PerReplica(vals)

# Note: nest.map_structure exercises nest.flatten and
# nest.pack_sequence_as.
result = nest.map_structure(
    lambda t: t + 10, per_replica, expand_composites=True)

self.assertLen(result.values, 2)
self.assertAllEqual(result.values[0], 11.)
self.assertAllEqual(result.values[1], [15., 16.0])
