# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/norm_op_test.py

def _CompareNorm(self, matrix):
    np_norm = np.linalg.norm(matrix, ord=ord_, axis=axis_, keepdims=keep_dims_)
    with self.cached_session() as sess:
        if use_static_shape_:
            tf_matrix = constant_op.constant(matrix)
            tf_norm = linalg_ops.norm(
                tf_matrix, ord=ord_, axis=axis_, keepdims=keep_dims_)
            tf_norm_val = self.evaluate(tf_norm)
        else:
            tf_matrix = array_ops.placeholder(dtype_)
            tf_norm = linalg_ops.norm(
                tf_matrix, ord=ord_, axis=axis_, keepdims=keep_dims_)
            tf_norm_val = sess.run(tf_norm, feed_dict={tf_matrix: matrix})
    self.assertAllClose(np_norm, tf_norm_val, rtol=1e-5, atol=1e-5)

@test_util.run_v1_only("b/120545219")
def Test(self):
    is_matrix_norm = (isinstance(axis_, tuple) or
                      isinstance(axis_, list)) and len(axis_) == 2
    is_fancy_p_norm = np.isreal(ord_) and np.floor(ord_) != ord_
    if ((not is_matrix_norm and ord_ == "fro") or
        (is_matrix_norm and is_fancy_p_norm)):
        self.skipTest("Not supported by neither numpy.linalg.norm nor tf.norm")
    if ord_ == "euclidean" or (axis_ is None and len(shape) > 2):
        self.skipTest("Not supported by numpy.linalg.norm")
    matrix = np.random.randn(*shape_).astype(dtype_)
    if dtype_ in (np.complex64, np.complex128):
        matrix += 1j * np.random.randn(*shape_).astype(dtype_)
    _CompareNorm(self, matrix)

exit(Test)
