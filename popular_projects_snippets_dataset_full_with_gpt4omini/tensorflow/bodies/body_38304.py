# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
with self.session(use_gpu=False):
    num_segments = 8327099846119777499
    unsorted = math_ops.unsorted_segment_sum(
        np.ones((3)), segment_ids=898042203, num_segments=num_segments)
    with self.assertRaisesOpError("Encountered overflow when multiplying"):
        self.evaluate(unsorted)
