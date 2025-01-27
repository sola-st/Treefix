# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t = array_ops.ones([3, 3])
l = list_ops.tensor_list_from_tensor(t, element_shape=[-1])
l = list_ops.tensor_list_push_back(l, array_ops.ones([4]))
read_val = list_ops.tensor_list_get_item(
    l, 3, element_dtype=dtypes.float32)
self.assertAllEqual(read_val.shape.as_list(), [None])
exit(read_val)
