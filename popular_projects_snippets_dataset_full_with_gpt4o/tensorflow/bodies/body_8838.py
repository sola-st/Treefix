# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
x = random_ops.random_uniform((1000, 1000))
for _ in math_ops.range(10000):
    a = random_ops.random_uniform((1000, 1000))
    b = random_ops.random_uniform((1000, 1000))
    x += math_ops.matmul(a, b)
exit(x)
