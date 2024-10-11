# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)
dist = _TestStrategy()
with dist.scope():
    self.assertIs(None, ds_context.get_replica_context())
    self.assertIs(dist, ds_context.get_cross_replica_context())
    self.assertTrue(ds_context.in_cross_replica_context())
    self.assertTrue(ds_context.has_strategy())
    self.assertIs(dist, ds_context.get_strategy())
    expected_value = _get_test_variable(
        "baz", variable_scope.VariableSynchronization.AUTO,
        variable_scope.VariableAggregation.NONE)
    self.assertDictEqual(expected_value,
                         variable_scope.variable(1.0, name="baz"))
_assert_in_default_state(self)
