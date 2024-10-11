# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
dataset = dataset_ops.Dataset.from_tensors([42]).unbatch(name="unbatch")
self.assertDatasetProduces(dataset, [42])
