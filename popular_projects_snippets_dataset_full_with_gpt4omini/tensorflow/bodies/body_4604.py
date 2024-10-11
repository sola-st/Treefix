# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/checkpoint_utils_test.py
v1 = variable_scope.get_variable("new_var1", [1, 10])
# Use string add to create new object in each replica
prefix = "new_"
suffix = "var1"
new_var1 = prefix + suffix
checkpoint_utils.init_from_checkpoint(checkpoint_dir, {
    "var1": new_var1,
})
with self.test_session(graph=g) as session:
    session.run(variables.global_variables_initializer())
    self.assertAllEqual(v1_value, self.evaluate(v1))
