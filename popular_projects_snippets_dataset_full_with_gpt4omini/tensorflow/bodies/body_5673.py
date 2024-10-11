# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if context.num_gpus() < 1 and context.executing_eagerly():
    self.skipTest("A GPU is not available for this test in eager mode.")
v, replica_local = _make_replica_local(
    variable_scope.VariableAggregation.SUM)

self.assertEqual(v[0].constraint, replica_local.constraint)
self.assertEqual(v[0].name, replica_local.name)
self.assertEqual(v[0].dtype, replica_local.dtype)
self.assertEqual(v[0].shape, replica_local.shape)
self.assertEqual(variable_scope.VariableAggregation.SUM,
                 replica_local.aggregation)
