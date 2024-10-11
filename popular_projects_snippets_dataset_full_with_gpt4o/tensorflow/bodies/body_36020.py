# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    init_value = np.ones((4, 4, 4))
    variable = resource_variable_ops.ResourceVariable(
        init_value,
        name="init",
        synchronization=variables.VariableSynchronization.ON_READ,
        aggregation=variables.VariableAggregation.SUM)

    copied_variable = copy.deepcopy(variable)
    self.assertEqual(variable.name, copied_variable.name)
    self.assertEqual(variable.shape, copied_variable.shape)
    self.assertEqual(variable.device, copied_variable.device)
    self.assertEqual(variable.synchronization,
                     copied_variable.synchronization)
    self.assertEqual(variable.aggregation, copied_variable.aggregation)

    # The copied variable should have the same value as the original.
    self.assertAllEqual(variable.numpy(), copied_variable.numpy())

    # Updates to the copy should not be reflected in the original.
    copied_variable.assign(4 * np.ones((4, 4, 4)))
    self.assertNotAllEqual(variable.numpy(), copied_variable.numpy())
