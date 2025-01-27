# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
indices_flat = np.array([0, 4, 0, 8, 3, 8, 4, 7, 7, 3])
num_segments = 12
for indices in indices_flat, indices_flat.reshape(5, 2):
    # Note that the GPU implem has different paths for different inner sizes.
    for inner_size in [1, 2, 3, 32]:
        shape = indices.shape + (inner_size,)

        ops_list = (
            self.complex_ops_list if dtype.is_complex else self.ops_list)
        tf_x, np_x = self._input(shape, dtype=dtype)
        for use_gpu in [True, False]:
            with self.cached_session():
                for np_op1, np_op2, tf_op, init_op in ops_list:
                    # sqrt_n doesn't support integers
                    if (np_op2 == self._sqrt_n_reduce_op and dtype.is_integer):
                        continue
                    np_ans = self._segmentReduce(
                        indices,
                        np_x,
                        np_op1,
                        np_op2,
                        num_segments=num_segments,
                        initial_value=init_op(dtype))
                    s = tf_op(tf_x, segment_ids=indices, num_segments=num_segments)
                    tf_ans = self.evaluate(s)
                    self.assertAllCloseAccordingToType(np_ans, tf_ans)
                    self.assertShapeEqual(np_ans, s)
