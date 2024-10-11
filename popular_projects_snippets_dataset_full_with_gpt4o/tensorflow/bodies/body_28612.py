# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
tensor = [[1, 2], [3, 4]]
dataset = dataset_ops.Dataset.from_tensor_slices(tensor).cache()
self.verifyRandomAccess(dataset, tensor)
