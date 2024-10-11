# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# The GPU implem has a special case when there is a single output.
for inner_size in (1, 2, 3, 32):
    with self.session():
        tf_ygrad, np_ygrad = self._input([3, inner_size],
                                         dtype=dtypes_lib.float32)
        segment_ids = [0, 1, 2, 2, 2]
        indices = [0, 0, 0, 0, 0]
        output_dim0 = 1
        ops_list = [
            (math_ops.sparse_segment_sum_grad, "sum"),
            (math_ops.sparse_segment_mean_grad, "mean"),
            (math_ops.sparse_segment_sqrt_n_grad, "sqrtn"),
        ]
        for tf_op, mode in ops_list:
            np_xgrad = self._sparseSegmentReduceGrad(np_ygrad, indices,
                                                     segment_ids, output_dim0,
                                                     mode)
            tf_xgrad = tf_op(tf_ygrad, indices, segment_ids, output_dim0)
            self.assertAllClose(tf_xgrad, np_xgrad)
