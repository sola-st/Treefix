# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.interleave(
    self._statefulDatasetFunc, num_parallel_calls=2)
self._assertNotCheckpointable(dataset)
