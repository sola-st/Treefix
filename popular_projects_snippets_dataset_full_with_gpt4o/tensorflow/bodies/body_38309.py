# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
tf_x, np_x = self._input([10, 4], dtype=dtypes_lib.float32)
ops_list = [(np.add, None, math_ops.sparse_segment_sum), (
    self._mean_cum_op, self._mean_reduce_op, math_ops.sparse_segment_mean)]
segment_indices = [0, 2, 2, 2]
tf_indices = [8, 3, 0, 9]
with self.session():
    for np_op1, np_op2, tf_op in ops_list:
        np_ans = self._sparseSegmentReduce(np_x, tf_indices, segment_indices,
                                           np_op1, np_op2)
        s = tf_op(data=tf_x, indices=tf_indices, segment_ids=segment_indices)
        tf_ans = self.evaluate(s)
        self.assertAllClose(np_ans, tf_ans)
