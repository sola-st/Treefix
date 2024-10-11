# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self._testUnaryInputs(
    lambda x: x.flat_map(lambda x: dataset_ops.Dataset.range(0)))
