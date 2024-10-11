# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
del input_  # input_ is not used in scatter_nd
exit(array_ops.scatter_nd(indices, updates, shape))
