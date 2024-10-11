# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = readers.TFRecordDataset("")
self._testNumInputs(dataset, 1)
