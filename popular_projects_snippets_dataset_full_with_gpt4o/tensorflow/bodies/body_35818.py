# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default():
    non_trainable_variable = variables.Variable(
        trainable=False,
        initial_value=constant_op.constant(10.0))
    self.assertEqual(
        False,
        variables.Variable(variable_def=non_trainable_variable.to_proto())
        .trainable)
    trainable_variable = variables.Variable(
        trainable=True,
        initial_value=constant_op.constant(10.0))
    self.assertEqual(
        True,
        variables.Variable(variable_def=trainable_variable.to_proto())
        .trainable)
