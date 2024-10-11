# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c0 = constant_op.constant([1.0, 2.0])
l = list_ops.tensor_list_scatter(c0, [1, 3], [])
# TensorListScatter should return a list with size largest index + 1.
self.assertAllEqual(list_ops.tensor_list_length(l), 4)
