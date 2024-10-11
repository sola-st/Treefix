# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
dataset = dataset_ops.Dataset.from_tensors(42).prefetch(1, name="prefetch")
self.assertDatasetProduces(dataset, [42])
