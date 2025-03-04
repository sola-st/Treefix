# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Note: the test is done by replacing segment_ids with 8 to -1
# for index  and replace values generated by numpy with 0.
indices_flat = np.array([0, 4, 0, 8, 3, 8, 4, 7, 7, 3])
num_segments = 12
for indices in indices_flat, indices_flat.reshape(5, 2):
    shape = indices.shape + (2,)
    for dtype in self.all_dtypes:
        with self.session():
            tf_x, np_x = self._input(shape, dtype=dtype)
            np_ans = self._segmentReduce(
                indices, np_x, np.add, op2=None, num_segments=num_segments)
            # Replace np_ans[8] with 0 for the value
            np_ans[8:] = 0
            # Replace 8 with -1 in indices
            np.place(indices, indices == 8, [-1])
            s = math_ops.unsorted_segment_sum(
                data=tf_x, segment_ids=indices, num_segments=num_segments)
            tf_ans = self.evaluate(s)
        self.assertAllClose(np_ans, tf_ans)
        self.assertShapeEqual(np_ans, s)
