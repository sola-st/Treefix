# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
exit(variable_scope.get_variable(
    "dummy", shape=[1], trainable=trainable,
    initializer=init_ops.zeros_initializer()))
