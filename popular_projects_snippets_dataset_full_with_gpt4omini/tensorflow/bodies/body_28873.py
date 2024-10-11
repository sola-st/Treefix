# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.map(self._statefulBoolFunc, num_parallel_calls=2)
self._assertNotCheckpointable(dataset)
