# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
x_1d = array_ops.reshape(x, [1])
x_2d = array_ops.reshape(x, [1, 1])
exit(sparse_tensor.SparseTensor(x_2d, x_1d, x_1d))
