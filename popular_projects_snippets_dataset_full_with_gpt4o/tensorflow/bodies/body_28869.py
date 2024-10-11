# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.flat_map(self._statefulDatasetFunc)
self._assertNotCheckpointable(dataset)
