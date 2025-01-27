# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
vals = (constant_op.constant(1.),)
per_replica = values_lib.PerReplica(vals)

spec = per_replica._type_spec
self.assertEqual(spec._value_specs,
                 (tensor_spec.TensorSpec([], dtypes.float32),))
