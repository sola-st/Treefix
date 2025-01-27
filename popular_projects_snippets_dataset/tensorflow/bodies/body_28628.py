# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(10)
self._testNumInputs(dataset, 0)
