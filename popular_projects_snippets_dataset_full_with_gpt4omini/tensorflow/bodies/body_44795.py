# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensor_list_test.py
l = []
l = tl.dynamic_list_append(l, 1)
self.assertListEqual(l, [1])

l = list_ops.empty_tensor_list(self._shape(()), dtypes.int32)
l = tl.dynamic_list_append(l, 1)
s = list_ops.tensor_list_stack(l, element_dtype=dtypes.int32)
self.assertAllEqual(s, [1])

l = tensor_array_ops.TensorArray(dtypes.int32, size=0, dynamic_size=True)
l = tl.dynamic_list_append(l, 1)
s = l.stack()
self.assertAllEqual(s, [1])

l = tl.TensorList(self._shape(()), dtypes.int32)
l = tl.dynamic_list_append(l, 1)
self.assertAllEqual(l[0], 1)
