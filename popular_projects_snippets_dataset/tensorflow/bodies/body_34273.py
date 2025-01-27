# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l1 = list_ops.tensor_list_from_tensor([1.0, 2.0], element_shape=[])
l2 = list_ops.tensor_list_from_tensor([3.0, 4.0], element_shape=[])
l3 = list_ops.tensor_list_from_tensor([5.0, 6.0], element_shape=[])
result = math_ops.add_n((l1, l2, l3))
result_t = list_ops.tensor_list_stack(result, element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(result_t), [9., 12.])
