# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
dataset = dataset_ops.Dataset.from_tensors(42).repeat(1, name="repeat")
self.assertDatasetProduces(dataset, [42])
