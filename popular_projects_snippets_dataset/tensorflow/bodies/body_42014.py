# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
a = random_ops.random_uniform([32, 32])
exit(math_ops.matmul(a, a))
