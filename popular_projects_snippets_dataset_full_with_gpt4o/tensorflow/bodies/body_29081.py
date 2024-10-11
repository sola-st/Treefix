# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
dataset = dataset_ops.Dataset.range(5, name="range")
self.assertDatasetProduces(dataset, list(range(5)))
