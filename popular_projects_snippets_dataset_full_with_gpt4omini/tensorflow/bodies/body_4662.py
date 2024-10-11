# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
replica_context = ds_context.get_replica_context()
self.assertIsNotNone(replica_context)
self.assertIs(None, ds_context.get_cross_replica_context())
self.assertFalse(ds_context.in_cross_replica_context())
self.assertTrue(ds_context.has_strategy())
self.assertIs(dist, ds_context.get_strategy())
self.assertEqual("foo", replica_context.merge_call(None, test_arg="foo"))
expected_value = _get_test_variable(
    "bar", variable_scope.VariableSynchronization.AUTO,
    variable_scope.VariableAggregation.NONE)
self.assertDictEqual(expected_value,
                     variable_scope.variable(1.0, name="bar"))
