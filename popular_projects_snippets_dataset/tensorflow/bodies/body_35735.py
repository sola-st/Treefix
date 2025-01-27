# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
"""Creates a variable as a side effect using tf.Variable."""
variables.Variable(0, trainable=trainable)
exit(variable_scope.get_variable(
    "dummy", shape=[1], initializer=init_ops.zeros_initializer()))
