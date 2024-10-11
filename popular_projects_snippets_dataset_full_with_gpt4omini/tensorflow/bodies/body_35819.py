# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default():
    original_variable = variables.Variable(
        initial_value=constant_op.constant(10.0),
        synchronization=variables.VariableSynchronization.NONE,
        aggregation=variables.VariableAggregationV2.ONLY_FIRST_REPLICA)
    self.assertEqual(variables.VariableSynchronization.NONE,
                     original_variable.synchronization)
    self.assertEqual(variables.VariableAggregation.ONLY_FIRST_REPLICA,
                     original_variable.aggregation)

    laundered = variables.Variable(
        variable_def=original_variable.to_proto())
    self.assertEqual(
        variables.VariableSynchronization.NONE,
        laundered.synchronization)
    self.assertEqual(variables.VariableAggregationV2.ONLY_FIRST_REPLICA,
                     laundered.aggregation)
