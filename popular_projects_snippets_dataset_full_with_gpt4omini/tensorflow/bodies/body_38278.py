# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Each item is np_op1, np_op2, tf_op
ops_list = [(np.add, None, math_ops.segment_sum),
            (self._mean_cum_op, self._mean_reduce_op,
             math_ops.segment_mean),
            (np.ndarray.__mul__, None, math_ops.segment_prod),
            (np.minimum, None, math_ops.segment_min),
            (np.maximum, None, math_ops.segment_max)]

# A subset of ops has been enabled for complex numbers
complex_ops_list = [(np.add, None, math_ops.segment_sum),
                    (np.ndarray.__mul__, None, math_ops.segment_prod),
                    (self._mean_cum_op, self._mean_reduce_op,
                     math_ops.segment_mean)]

n = 10
# Note that the GPU implem has different paths for different inner sizes.
for shape in [[n, 1], [n, 2], [n, 3], [n, 32]]:
    indices = [i // 3 for i in range(n)]
    if dtype in (dtypes_lib.complex64, dtypes_lib.complex128):
        curr_ops_list = complex_ops_list
    else:
        curr_ops_list = ops_list
    for use_gpu in [True, False]:
        with self.cached_session(use_gpu=use_gpu):
            tf_x, np_x = self._input(shape, dtype=dtype)
            for np_op1, np_op2, tf_op in curr_ops_list:
                initial_value = 1 if tf_op is math_ops.segment_prod else 0
                np_ans = self._segmentReduce(
                    indices, np_x, np_op1, np_op2, initial_value=initial_value)
                s = tf_op(data=tf_x, segment_ids=indices)
                tf_ans = self.evaluate(s)
                self.assertAllCloseAccordingToType(np_ans, tf_ans)
                # NOTE(mrry): The static shape inference that computes
                # `tf_ans.shape` can only infer that sizes from dimension 1
                # onwards, because the size of dimension 0 is data-dependent
                # and may therefore vary dynamically.
                self.assertAllEqual(np_ans.shape[1:], tf_ans.shape[1:])
