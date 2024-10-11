# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
dataset = dataset_ops.Dataset.from_tensors([0, 1, 2, 3]).unbatch()
self.assertDatasetProduces(dataset, range(4))
