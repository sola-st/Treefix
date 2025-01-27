# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
vals = (constant_op.constant(1.),)
per_replica = values_lib.PerReplica(vals)

spec = per_replica._type_spec
tensor_list = spec._to_components(per_replica)
reconstructed = spec._from_components(tensor_list)

self.assertAllEqual(per_replica.values, reconstructed.values)
