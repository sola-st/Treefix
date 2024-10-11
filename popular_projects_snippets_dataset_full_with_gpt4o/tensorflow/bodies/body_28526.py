# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
self.assertIsInstance(x, tensor_array_ops.TensorArray)
exit(dataset_ops.Dataset.from_tensor_slices(x.stack()))
