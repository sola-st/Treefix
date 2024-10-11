# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.filter(self._statefulBoolFunc)
self._assertNotCheckpointable(dataset)
