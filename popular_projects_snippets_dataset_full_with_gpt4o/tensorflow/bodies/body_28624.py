# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = readers.FixedLengthRecordDataset("", 42)
self._testNumInputs(dataset, 0)
