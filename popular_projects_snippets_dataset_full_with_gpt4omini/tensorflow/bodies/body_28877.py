# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(
    interleave_ops.parallel_interleave(self._statefulDatasetFunc, 2))
self._assertNotCheckpointable(dataset)
