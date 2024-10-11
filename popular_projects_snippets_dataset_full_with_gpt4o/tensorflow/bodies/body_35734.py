# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
with variable_scope.variable_scope(scope_name):
    exit(variable_scope.get_variable(
        "dummy", shape=[1], initializer=init_ops.zeros_initializer()))
