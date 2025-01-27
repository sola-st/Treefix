# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# non-differentiable operation with custom gradient.
# The variable should be found.
y = _MyOnesLike(var)
exit(array_ops.identity(x) + 5.0 + y)
