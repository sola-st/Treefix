# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [4, 4]
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        tf_x, _ = self._input(shape)
        indices = [0, 1]
        s = math_ops.segment_sum(data=tf_x, segment_ids=indices)
        with self.assertRaisesOpError("segment_ids should be the same size"):
            self.evaluate(s)
