# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
dataset = dataset_ops.Dataset.range(10).prefetch(buffer_size=buffer_size)
self.assertDatasetProduces(dataset, expected_output=range(10))
