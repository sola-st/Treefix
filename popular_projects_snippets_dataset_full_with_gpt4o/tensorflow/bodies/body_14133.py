# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
my_zeros = array_ops.zeros(my_shape)
exit(structured_array_ops._structured_tensor_like(my_zeros))
