# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_from_tensor([1., 2., 3.], element_shape=[])
l = list_ops.tensor_list_resize(l, 2)
self.assertEqual(self.evaluate(list_ops.tensor_list_length(l)), 2)
self.assertAllEqual(
    self.evaluate(
        list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)),
    [1., 2.])
