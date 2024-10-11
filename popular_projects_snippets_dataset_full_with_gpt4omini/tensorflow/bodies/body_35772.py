# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
w = variable_scope.get_variable(
    "w", shape=[1], initializer=init_ops.zeros_initializer())
exit(inputs * w)
