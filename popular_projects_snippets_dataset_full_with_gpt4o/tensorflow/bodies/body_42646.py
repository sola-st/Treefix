# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
x = array_ops.ones([1000, 1000])
for _ in range(1, 1000):
    x = x * x
variable_b.assign_add(i)
a = 1.0 + variable_b
exit(a)
