# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/checkpoint_utils_test.py
v1 = variable_scope.get_variable("new_var1", [1, 10])
v2 = variable_scope.get_variable(
    "new_var2", [10, 10],
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=variable_scope.VariableAggregation.MEAN)
checkpoint_utils.init_from_checkpoint(checkpoint_dir, {
    "var1": "new_var1",
    "var2": "new_var2"
})
with self.session(graph=g) as session:
    session.run(variables.global_variables_initializer())
    self.assertAllEqual(v1_value, self.evaluate(v1))
    self.assertAllEqual(v2_value, self.evaluate(v2))
