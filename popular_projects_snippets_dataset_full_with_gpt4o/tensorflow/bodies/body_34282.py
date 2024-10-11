# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=[5, 2])
t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(t).shape, (0, 2))
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=[None, 2])
t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(t).shape, (0, 2))
