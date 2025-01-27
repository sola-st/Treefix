# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_inverse_op_test.py
for adjoint in False, True:
    y = x.astype(np_type)
    with self.session() as sess:
        # Verify that x^{-1} * x == Identity matrix.
        p = array_ops.placeholder(dtypes.as_dtype(y.dtype), y.shape, name="x")
        with self.test_scope():
            inv = linalg_ops.matrix_inverse(p, adjoint=adjoint)
            tf_ans = math_ops.matmul(inv, p, adjoint_b=adjoint)
            np_ans = np.identity(y.shape[-1])
            if x.ndim > 2:
                tiling = list(y.shape)
                tiling[-2:] = [1, 1]
                np_ans = np.tile(np_ans, tiling)
        out = sess.run(tf_ans, feed_dict={p: y})
        self.assertAllClose(np_ans, out, rtol=1e-3, atol=1e-3)
        self.assertShapeEqual(y, tf_ans)
