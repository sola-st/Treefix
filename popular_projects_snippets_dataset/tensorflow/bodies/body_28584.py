# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(10).cache().take(5).repeat(2)

expected_output = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
self.assertDatasetProduces(dataset, expected_output=expected_output)
