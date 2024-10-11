# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)
dist = _TestStrategy()
with dist.scope():
    expected_value = _get_test_variable(
        "baz", variable_scope.VariableSynchronization.ON_WRITE,
        variable_scope.VariableAggregation.MEAN)
    self.assertDictEqual(
        expected_value,
        variable_scope.variable(
            1.0,
            name="baz",
            synchronization=variable_scope.VariableSynchronization.ON_WRITE,
            aggregation=variable_scope.VariableAggregation.MEAN))
_assert_in_default_state(self)
