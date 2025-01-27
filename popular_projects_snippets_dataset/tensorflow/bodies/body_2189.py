# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
var0 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)
var1 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)
grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
grads1 = constant_op.constant([0.02, 0.04], dtype=dtype)

exit((var0, var1, grads0, grads1))
