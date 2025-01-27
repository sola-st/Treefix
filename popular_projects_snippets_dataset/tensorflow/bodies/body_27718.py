# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
dataset = dataset_ops.Dataset.from_tensors(42).skip(0, name="skip")
self.assertDatasetProduces(dataset, [42])
