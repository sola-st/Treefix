# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
dataset = dataset_ops.Dataset.from_tensors(42).window(
    1, name="window").flat_map(lambda x: x)
self.assertDatasetProduces(dataset, [42])
