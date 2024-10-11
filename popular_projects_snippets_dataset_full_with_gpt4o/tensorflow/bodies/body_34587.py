# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
indices = constant_op.constant([1, 8])
w = ta.unstack(values)
g = w.gather(indices)
exit(g)
