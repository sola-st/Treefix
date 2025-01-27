# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_test.py
dataset = dataset_ops.Dataset.from_tensors(42).take(1, name="take")
self.assertDatasetProduces(dataset, [42])
