# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
variable_scope.get_local_variable(
    "local", shape=[1], initializer=init_ops.zeros_initializer())
exit(variable_scope.get_variable(
    "dummy", shape=[1], initializer=init_ops.zeros_initializer()))
