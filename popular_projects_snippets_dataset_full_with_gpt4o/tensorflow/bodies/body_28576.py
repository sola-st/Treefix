# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(10).cache(self.cache_prefix)
dataset = dataset.map(lambda a: a).batch(4).repeat(2)
expected_output = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]] * 2
self.assertDatasetProduces(dataset, expected_output)
