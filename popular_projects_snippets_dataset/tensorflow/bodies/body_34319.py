# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
x_prod = constant_op.constant([1.])
for unused_i in math_ops.range(3):
    x_prod = x_prod * x
exit(x_prod)
