# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.Graph().as_default():
    non_trainable_variable = resource_variable_ops.ResourceVariable(
        trainable=False,
        initial_value=constant_op.constant(10.0))
    self.assertEqual(
        False,
        resource_variable_ops.ResourceVariable(
            variable_def=non_trainable_variable.to_proto())
        .trainable)
    trainable_variable = resource_variable_ops.ResourceVariable(
        trainable=True,
        initial_value=constant_op.constant(10.0))
    self.assertEqual(
        True,
        resource_variable_ops.ResourceVariable(
            variable_def=trainable_variable.to_proto())
        .trainable)
