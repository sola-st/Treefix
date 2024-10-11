# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(([1, 2], [3, 4], [5, 6]))
self.assertEqual((1, 3, 5), self.evaluate(random_access.at(dataset, 0)))
self.assertEqual((2, 4, 6), self.evaluate(random_access.at(dataset, 1)))
