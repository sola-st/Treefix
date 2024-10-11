# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/simple_save_test.py
self.assertEqual(actual_tensor_info.name, expected_tensor.name)
self.assertEqual(actual_tensor_info.dtype, expected_tensor.dtype)
self.assertEqual(
    len(actual_tensor_info.tensor_shape.dim), len(expected_tensor.shape))
for i in range(len(actual_tensor_info.tensor_shape.dim)):
    self.assertEqual(actual_tensor_info.tensor_shape.dim[i].size,
                     expected_tensor.shape[i])
