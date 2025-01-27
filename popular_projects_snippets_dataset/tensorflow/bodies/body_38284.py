# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [4, 4]
with self.cached_session():
    tf_x, _ = self._input(shape)
    indices = [-1, -1, 0, 0]
    s = math_ops.segment_sum(data=tf_x, segment_ids=indices)
    with self.assertRaisesOpError(
        r"Segment id -1 out of range \[0, 1\), possibly because "
        "'segment_ids' input is not sorted."):
        self.evaluate(s)
