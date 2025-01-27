# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.from_tensors(42).cache(name="cache")
self.assertDatasetProduces(dataset, [42])
