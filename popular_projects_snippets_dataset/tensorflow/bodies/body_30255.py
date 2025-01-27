# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
items = 1
for dim in shape:
    items *= dim
var = variables.Variable(
    array_ops.reshape(math_ops.linspace(1., float(items), items), shape),
    dtype=dtype)
exit(var)
