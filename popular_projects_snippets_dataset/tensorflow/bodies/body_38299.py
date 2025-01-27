# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Strategy: compute the gradient for UnsortedSegmentSum and SegmentSum
# and compare the outputs, which should be identical.
# NB: for this test to work, indices must be valid for SegmentSum, namely
# it must be sorted, the indices must be contiguous, and num_segments
# must be max(indices) + 1.
indices = [0, 0, 1, 1, 1, 2, 3, 4, 5]
n = len(indices)
num_cols = 2
shape = [n, num_cols]
num_segments = max(indices) + 1
for dtype in self.differentiable_dtypes:
    with self.cached_session():
        tf_x, np_x = self._input(shape, dtype=dtype)
        # Results from UnsortedSegmentSum
        unsorted_s = math_ops.unsorted_segment_sum(
            data=tf_x, segment_ids=indices, num_segments=num_segments)
        unsorted_jacob_t, unsorted_jacob_n = (
            gradient_checker.compute_gradient(tf_x, shape, unsorted_s,
                                              [num_segments, num_cols],
                                              x_init_value=np_x, delta=1))

        # Results from SegmentSum
        sorted_s = math_ops.segment_sum(data=tf_x, segment_ids=indices)
        sorted_jacob_t, sorted_jacob_n = gradient_checker.compute_gradient(
            tf_x,
            shape,
            sorted_s, [num_segments, num_cols],
            x_init_value=np_x,
            delta=1)
    self.assertAllClose(unsorted_jacob_t, sorted_jacob_t)
    self.assertAllClose(unsorted_jacob_n, sorted_jacob_n)
