# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
with self.assertRaises(ValueError):
    data_structures.tf_tensor_array_new([3, 4.0])
with self.assertRaises(ValueError):
    data_structures.tf_tensor_array_new([3, 4], element_dtype=dtypes.float32)
with self.assertRaises(ValueError):
    data_structures.tf_tensor_array_new([3, [4, 5]])
with self.assertRaises(ValueError):
    data_structures.tf_tensor_array_new([3, 4], element_shape=(2,))
with self.assertRaises(ValueError):
    data_structures.tf_tensor_array_new([], element_shape=(2,))
# TAs can infer the shape.
self.assertIsNot(
    data_structures.tf_tensor_array_new([], element_dtype=dtypes.float32),
    None)
