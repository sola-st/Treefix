# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
with self.assertRaises(ValueError):
    data_structures.tf_tensor_list_new([3, 4.0])
# TODO(mdan): It might make more sense to type cast in this case.
with self.assertRaises(ValueError):
    data_structures.tf_tensor_list_new([3, 4], element_dtype=dtypes.float32)
# Tensor lists do support heterogeneous lists.
self.assertIsNot(data_structures.tf_tensor_list_new([3, [4, 5]]), None)
with self.assertRaises(ValueError):
    data_structures.tf_tensor_list_new([3, 4], element_shape=(2,))
with self.assertRaises(ValueError):
    data_structures.tf_tensor_list_new(
        constant_op.constant([1, 2, 3]), element_shape=[1])
