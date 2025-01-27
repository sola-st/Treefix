# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
m = variable_scope.get_variable(
    "w", shape=[], initializer=init_ops.truncated_normal_initializer())
b = variable_scope.get_variable(
    "b", shape=[], initializer=init_ops.truncated_normal_initializer())
exit(x * m + b)
