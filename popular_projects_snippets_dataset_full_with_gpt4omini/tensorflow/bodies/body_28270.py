# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
x = math_ops.add(x, 1)
random_ops.random_shuffle([x, math_ops.square(x)])
exit(x)
