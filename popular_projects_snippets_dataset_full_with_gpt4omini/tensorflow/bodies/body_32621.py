# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
for adjoint in False, True:
    y = x.astype(np_type)
    with self.cached_session(use_gpu=test_util.is_gpu_available()):
        # Verify that x^{-1} * x == Identity matrix.
        inv = linalg_ops.matrix_inverse(y, adjoint=adjoint)
        tf_ans = self._high_precision_matmul(inv, y, adjoint_b=adjoint)
        np_ans = np.identity(y.shape[-1]).astype(np_type)
        if x.ndim > 2:
            tiling = list(y.shape)
            tiling[-2:] = [1, 1]
            np_ans = np.tile(np_ans, tiling)
        out = self.evaluate(tf_ans)
        self.assertAllCloseAccordingToType(
            np_ans, out, atol=0.001, half_atol=0.1)
        self.assertShapeEqual(y, tf_ans)
