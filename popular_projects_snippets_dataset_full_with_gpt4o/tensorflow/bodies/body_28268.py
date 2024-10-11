# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, lambda x: [x, "hello", 10])
self.assertDatasetProduces(dataset, [(i, b"hello", 10) for i in range(10)])
