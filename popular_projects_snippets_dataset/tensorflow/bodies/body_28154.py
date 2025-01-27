# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
dataset = dataset_ops.Dataset.from_tensors(42).unique(name="unique")
self.assertDatasetProduces(dataset, [42])
