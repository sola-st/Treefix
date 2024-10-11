# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
dtypes = [
    dtypes_lib.float32,
    dtypes_lib.float64,
    dtypes_lib.int64,
    dtypes_lib.int32,
    dtypes_lib.bfloat16,
]

index_dtypes = [dtypes_lib.int32, dtypes_lib.int64]
segment_ids_dtypes = [dtypes_lib.int32, dtypes_lib.int64]

mean_dtypes = [dtypes_lib.float32, dtypes_lib.float64]

# Each item is np_op1, np_op2, tf_op
ops_list = [(np.add, None, math_ops.sparse_segment_sum),
            (self._mean_cum_op, self._mean_reduce_op,
             math_ops.sparse_segment_mean)]

n = 400
# Note that the GPU implem has different paths for different inner sizes.
for inner_size in [1, 2, 3, 32]:
    shape = [n, inner_size]
    segment_indices = []
    for i in range(20):
        for _ in range(i + 1):
            segment_indices.append(i)
    num_indices = len(segment_indices)
    for dtype in dtypes:
        for index_dtype in index_dtypes:
            for segment_ids_dtype in segment_ids_dtypes:
                with self.cached_session():
                    tf_indices, np_indices, tf_x, np_x = self._sparse_input(
                        shape, num_indices, dtype=dtype)
                    for np_op1, np_op2, tf_op in ops_list:
                        if (tf_op == math_ops.sparse_segment_mean and
                            dtype not in mean_dtypes):
                            continue
                        np_ans = self._sparseSegmentReduce(np_x, np_indices,
                                                           segment_indices, np_op1,
                                                           np_op2)
                        s = tf_op(
                            data=tf_x,
                            indices=math_ops.cast(tf_indices, index_dtype),
                            segment_ids=math_ops.cast(segment_indices,
                                                      segment_ids_dtype))
                        tf_ans = self.evaluate(s)
                        self.assertAllCloseAccordingToType(np_ans, tf_ans)
                        # NOTE(mrry): The static shape inference that computes
                        # `tf_ans.shape` can only infer that sizes from dimension 1
                        # onwards, because the size of dimension 0 is data-dependent
                        # and may therefore vary dynamically.
                        self.assertAllEqual(np_ans.shape[1:], tf_ans.shape[1:])
