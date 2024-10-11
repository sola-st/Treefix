# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
a = dataset_ops.Dataset.range(5).window(1)
b = dataset_ops.Dataset.range(5, 10).window(1)
c = a.concatenate(b).flat_map(lambda x: x)
self.assertDatasetProduces(c, list(range(10)))
