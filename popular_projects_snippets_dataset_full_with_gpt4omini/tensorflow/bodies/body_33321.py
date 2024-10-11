# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
with self.session() as sess:
    inp = array_ops.placeholder(ops.dtypes.float32)
    expm = linalg_impl.matrix_exponential(inp)
    matrix = np.array([[1., 2.], [3., 4.]])
    sess.run(expm, feed_dict={inp: matrix})
