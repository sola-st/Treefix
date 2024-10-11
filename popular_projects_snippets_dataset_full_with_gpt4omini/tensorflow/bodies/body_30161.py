# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
n = 256
shape = (n, n, n)
items = n**3
var = variables.Variable(
    array_ops.reshape(math_ops.linspace(1., float(items), items), shape),
    dtype=dtypes.float32)
exit(var)
