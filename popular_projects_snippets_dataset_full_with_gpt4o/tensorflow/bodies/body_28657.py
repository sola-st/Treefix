# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(5).map(lambda x: x * 2)
self.assertLen(dataset._functions(), 1)
