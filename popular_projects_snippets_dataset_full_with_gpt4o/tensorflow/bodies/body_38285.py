# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [4, 4]
with self.cached_session():
    tf_x, _ = self._input(shape)
    indices = [0, 1, 0, 1]
    s = math_ops.segment_sum(data=tf_x, segment_ids=indices)
    with self.assertRaisesOpError("segment ids are not increasing"):
        self.evaluate(s)
