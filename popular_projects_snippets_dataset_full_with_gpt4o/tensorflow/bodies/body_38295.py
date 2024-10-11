# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
num_cols = 2
indices_flat = np.array([0, 4, 0, -1, 3, -1, 4, 7, 7, 3])
num_segments = max(indices_flat) + 3
for dtype in self.differentiable_dtypes:
    ops_list = self.complex_ops_list if dtype.is_complex else self.ops_list
    for indices in indices_flat, indices_flat.reshape(5, 2):
        shape = indices.shape + (num_cols,)
        # test CPU and GPU as tf.gather behaves differently on each device
        for use_gpu in [False, True]:
            with self.cached_session(use_gpu=use_gpu):
                for _, _, tf_op, _ in ops_list:
                    tf_x, np_x = self._input(shape, dtype=dtype)
                    s = tf_op(tf_x, indices, num_segments)
                    jacob_t, jacob_n = gradient_checker.compute_gradient(
                        tf_x,
                        shape,
                        s, [num_segments, num_cols],
                        x_init_value=np_x,
                        delta=1.)
                    self.assertAllCloseAccordingToType(jacob_t, jacob_n,
                                                       half_atol=1e-2)
