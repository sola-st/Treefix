# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
feed_dict = {placeholder_a: a, placeholder_ca: clean_a, placeholder_b: b}
verification_np = sess.run(verification, feed_dict)
broadcasted_shape = a.shape[:-2] + (b.shape[-2], b.shape[-1])
broadcasted_b = b + np.zeros(shape=broadcasted_shape, dtype=b.dtype)
self.assertAllClose(broadcasted_b, verification_np, atol=atol)
