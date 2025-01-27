# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
super(ParallelInterleaveCheckpointTest, self).setUp()
self.input_values = np.array([2, 3], dtype=np.int64)
self.num_repeats = 2
self.num_outputs = np.sum(self.input_values) * 2
