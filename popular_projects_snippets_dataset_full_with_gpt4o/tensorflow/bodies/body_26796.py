# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
del x
v.assign(1.)
exit(dataset_ops.Dataset.range(2))
