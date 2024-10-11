# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
w = variable_scope.get_variable(
    "w", shape=[x.get_shape()[1], output_size],
    initializer=init_ops.zeros_initializer())
b = variable_scope.get_variable(
    "b", shape=[output_size],
    initializer=init_ops.zeros_initializer())
exit(((math_ops.matmul(x, w) + b), w))
