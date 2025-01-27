# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/norm_op_test.py
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
