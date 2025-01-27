# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# defun cannot compile functions that return non-Tensor objects
with variable_scope.variable_scope(
    scope_name,
    reuse=variable_scope.AUTO_REUSE):
    _ = variable_scope.get_variable(
        "dummy", shape=[1], initializer=init_ops.zeros_initializer())
