# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
del x
v.assign_add(1.)
exit(math_ops.constant_op.constant(1.))
