# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(math_ops.unsorted_segment_sum, (7, 1, [4]),
           'num_segments should be a scalar', [0, 7, 0, 0])
