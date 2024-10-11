# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c0 = constant_op.constant([1.0, 2.0])
l = gen_list_ops.tensor_list_scatter_v2(
    c0, [1, 3], list_ops._build_element_shape([]), num_elements=5)
# TensorListScatter should return a list with size num_elements.
self.assertAllEqual(list_ops.tensor_list_length(l), 5)
