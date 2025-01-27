# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# non-differentiable dependency on var.
# the variable should not be found.
y = array_ops.ones_like(var)
exit(array_ops.identity(x) + 5.0 + y)
