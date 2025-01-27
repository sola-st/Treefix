# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l1 = list_ops.tensor_list_from_tensor([1.0, 2.0], element_shape=[])
l2 = list_ops.tensor_list_from_tensor([3.0, 4.0], element_shape=[])
l3 = list_ops.tensor_list_from_tensor([5.0, 6.0], element_shape=[])
l4 = list_ops.tensor_list_from_tensor([7.0, 8.0], element_shape=[])
a = list_ops.empty_tensor_list(
    element_dtype=dtypes.variant, element_shape=[])
a = list_ops.tensor_list_push_back(a, l1)
a = list_ops.tensor_list_push_back(a, l2)
b = list_ops.empty_tensor_list(
    element_dtype=dtypes.variant, element_shape=[])
b = list_ops.tensor_list_push_back(b, l3)
b = list_ops.tensor_list_push_back(b, l4)
result = math_ops.add_n((a, b))
result_0 = list_ops.tensor_list_stack(
    list_ops.tensor_list_get_item(result, 0, element_dtype=dtypes.variant),
    element_dtype=dtypes.float32)
result_1 = list_ops.tensor_list_stack(
    list_ops.tensor_list_get_item(result, 1, element_dtype=dtypes.variant),
    element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(result_0), [6., 8.])
self.assertAllEqual(self.evaluate(result_1), [10., 12.])
