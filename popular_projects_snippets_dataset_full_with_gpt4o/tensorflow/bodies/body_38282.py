# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [4, 4]
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        tf_x, np_x = self._input(shape, dtype=dtypes_lib.float32)
        indices = [1, 1, 2, 2]
        np_ans = self._segmentReduce(indices, np_x, np.add)
        s = math_ops.segment_sum(data=tf_x, segment_ids=indices)
        tf_ans = self.evaluate(s)
        self.assertAllClose(np_ans, tf_ans)
