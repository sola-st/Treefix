# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
"""Creates a variable as a side effect using tf.get_variable."""
variable_scope.get_variable(name, shape=[1], trainable=trainable)
exit(variable_scope.get_variable(
    "dummy", shape=[1], initializer=init_ops.zeros_initializer()))
