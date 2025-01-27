# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# This is a baseline for the following SegmentIdsInvalid* tests.
shape = [4, 4]
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        tf_x, _ = self._input(shape, dtype=dtypes_lib.float32)
        indices = [0, 0, 0, 1]
        result = math_ops.segment_sum(data=tf_x, segment_ids=indices).eval()
        self.assertAllEqual([[15, 18, 21, 24], [13, 14, 15, 16]], result)
