# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
v.assign_add(1.)
exit((x, v.read_value()))
