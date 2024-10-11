# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
e0 = gen_list_ops.tensor_list_get_item(
    l, 0, element_shape=[], element_dtype=dtypes.float32)
e1 = gen_list_ops.tensor_list_get_item(
    l, 1, element_shape=[2, 3], element_dtype=dtypes.float32)
self.assertEqual(e0.shape.as_list(), [])
self.assertEqual(e1.shape.as_list(), [2, 3])
self.assertEqual(self.evaluate(e0), 0.)
self.assertAllEqual(self.evaluate(e1), np.zeros((2, 3)))

l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[None, 3], num_elements=3)
e1 = gen_list_ops.tensor_list_get_item(
    l, 1, element_shape=[2, 3], element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(e1), np.zeros((2, 3)))
