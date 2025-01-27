# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
if p is None:
    rank = x.ndim
    perm = (rank - 1) - np.arange(rank)
else:
    perm = p
np_ans = self._np_transpose(x, perm)
if conjugate:
    np_ans = np.conj(np_ans)
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    y = array_ops.transpose(inx, p, conjugate=conjugate)
    tf_ans = self.evaluate(y)

    self.assertAllEqual(np_ans, tf_ans)
    self.assertShapeEqual(np_ans, y)

    jacob_t = None
    # Gradient check on GPU.
    if x.dtype == np.float32:
        jacob_t, jacob_n = gradient_checker_v2.compute_gradient(
            lambda x: array_ops.transpose(x, p, conjugate=conjugate), [inx])
        self.assertAllClose(jacob_t, jacob_n, 1e-3, 1e-3)
    elif x.dtype == np.float64:
        jacob_t, jacob_n = gradient_checker_v2.compute_gradient(
            lambda x: array_ops.transpose(x, p, conjugate=conjugate), [inx])
        self.assertAllClose(jacob_t, jacob_n, 1e-6, 1e-6)

    exit((tf_ans, jacob_t))
