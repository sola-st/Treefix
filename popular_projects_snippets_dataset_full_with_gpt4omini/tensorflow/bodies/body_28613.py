# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    ([1, 2], [3, 4], [5, 6])).cache()
expected = [(1, 3, 5), (2, 4, 6)]
self.verifyRandomAccess(dataset, expected)
