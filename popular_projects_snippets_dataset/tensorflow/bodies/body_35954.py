# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    _ = variable_scope.get_variable("testGetTrainableVariables_a", [])
    with variable_scope.variable_scope(
        "testGetTrainableVariables_foo") as scope:
        _ = variable_scope.get_variable("testGetTrainableVariables_b", [])
        _ = variable_scope.get_variable(
            "testGetTrainableVariables_c", [], trainable=False)

        # sync `ON_READ` sets trainable=False
        _ = variable_scope.get_variable(
            "testGetTrainableVariables_d", [],
            synchronization=variable_scope.VariableSynchronization.ON_READ)
        self.assertEqual(
            [v.name for v in scope.trainable_variables()],
            ["testGetTrainableVariables_foo/testGetTrainableVariables_b:0"])

        _ = variable_scope.get_variable(
            "testGetTrainableVariables_e", [],
            synchronization=variable_scope.VariableSynchronization.ON_READ,
            trainable=True)
        self.assertEqual([v.name for v in scope.trainable_variables()], [
            "testGetTrainableVariables_foo/testGetTrainableVariables_b:0",
            "testGetTrainableVariables_foo/testGetTrainableVariables_e:0",
        ])

        # All other sync values sets trainable=True
        _ = variable_scope.get_variable(
            "testGetTrainableVariables_f", [],
            synchronization=variable_scope.VariableSynchronization.ON_WRITE)
        self.assertEqual([v.name for v in scope.trainable_variables()], [
            "testGetTrainableVariables_foo/testGetTrainableVariables_b:0",
            "testGetTrainableVariables_foo/testGetTrainableVariables_e:0",
            "testGetTrainableVariables_foo/testGetTrainableVariables_f:0",
        ])
