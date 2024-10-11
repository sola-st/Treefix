# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
dataset = dataset_ops.Dataset.from_tensors(42).scan(
    0, lambda x, y: (y, y), name="scan")
self.assertDatasetProduces(dataset, [42])
