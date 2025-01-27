# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
with self.session(use_gpu=False):
    data = np.ones((2, 1), dtype=np.float32)
    segment_ids = np.array([-1, -1], dtype=np.int32)
    unsorted = math_ops.unsorted_segment_sum(data, segment_ids, 2)
    self.assertAllClose(unsorted.eval(), np.zeros((2, 1), dtype=np.float32))
