# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# additional test for the prod gradient to ensure correct handling of zeros
values = np.array([0, 0, 1, 0, 2, 2, 3, 3, 3], dtype=np.float32)
indices = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2], dtype=np.int32)
indices_neg = np.array([-1, 0, 0, -1, 1, 1, -1, 2, 2], dtype=np.int32)
values_tf = constant_op.constant(values)
# ground truth partial derivatives
gradients_indices = np.zeros((9, 3), dtype=np.float32)
gradients_indices_neg = np.zeros((9, 3), dtype=np.float32)
# the derivative w.r.t. to the other segments is zero, so here we only
# explicitly set the grad values for the corresponding segment
gradients_indices[range(9), indices] = [0, 0, 0, 4, 0, 0, 9, 9, 9]
gradients_indices_neg[range(9), indices_neg] = [0, 1, 0, 0, 2, 2, 0, 3, 3]
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        for ind, grad_gt in [(indices, gradients_indices),
                             (indices_neg, gradients_indices_neg)]:
            s = math_ops.unsorted_segment_prod(values_tf,
                                               constant_op.constant(ind), 3)
            jacob_t, jacob_n = gradient_checker.compute_gradient(
                values_tf, (9,), s, (3,), x_init_value=values, delta=1)
            self.assertAllClose(jacob_t, jacob_n)
            self.assertAllClose(jacob_t, grad_gt)
