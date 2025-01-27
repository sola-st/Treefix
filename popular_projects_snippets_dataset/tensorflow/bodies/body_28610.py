# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(10).cache()
expected_elements = list(range(10))
self.verifyRandomAccess(dataset, expected_elements)
