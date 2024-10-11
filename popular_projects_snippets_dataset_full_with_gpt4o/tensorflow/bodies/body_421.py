# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session():
    mat = [[1., 2.], [2., 3.]]
    batched_mat = tf.expand_dims(mat, [0])
    result = tf.matmul(mat, mat).eval()
    result_batched = tf.batch_matmul(batched_mat, batched_mat).eval()
    self.assertAllEqual(result_batched, np.expand_dims(result, 0))
    self.assertAllEqual(
        tf.svd(mat, False, True).eval(),
        tf.svd(mat, compute_uv=False, full_matrices=True).eval())
