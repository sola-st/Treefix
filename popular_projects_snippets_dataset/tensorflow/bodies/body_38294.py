# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
dtypes = [dtypes_lib.int32, dtypes_lib.int64]
indices_flat = np.array([0, 4, 0, 8, 3, 8, 4, 7, 7, 3])
num_segments = 12
for indices in indices_flat, indices_flat.reshape(5, 2):
    shape = indices.shape + (2,)
    for dtype in dtypes:
        with self.cached_session():
            tf_x, np_x = self._input(shape)
            num_segments_constant = constant_op.constant(
                num_segments, dtype=dtype)
            np_ans = self._segmentReduce(
                indices, np_x, np.add, op2=None, num_segments=num_segments)
            s = math_ops.unsorted_segment_sum(
                data=tf_x,
                segment_ids=indices,
                num_segments=num_segments_constant)
            tf_ans = self.evaluate(s)
        self.assertAllClose(np_ans, tf_ans)
        self.assertShapeEqual(np_ans, s)
