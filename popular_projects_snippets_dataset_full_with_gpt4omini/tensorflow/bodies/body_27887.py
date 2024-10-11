# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
dataset = dataset_ops.Dataset.from_tensors(42, name="from_tensors")
self.assertDatasetProduces(dataset, [42])
