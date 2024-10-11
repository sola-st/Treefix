# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.from_tensors(42).filter(
    lambda x: True, name="filter")
self.assertDatasetProduces(dataset, [42])
