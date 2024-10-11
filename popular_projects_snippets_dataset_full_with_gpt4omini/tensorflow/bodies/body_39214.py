# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
with self.cached_session(use_gpu=False):
    tf_x = math_ops.cast(x, x_dtype)
    tf_y = math_ops.cast(y, y_dtype)
    tf_ans = math_ops.matmul(
        tf_x,
        tf_y,
        transpose_a=tr_a,
        transpose_b=tr_b,
        a_is_sparse=sp_a,
        b_is_sparse=sp_b)
    out = self.evaluate(tf_ans)
    np_x = math_ops.cast(tf_x, dtypes.float32).eval()
    np_y = math_ops.cast(tf_y, dtypes.float32).eval()

if tr_a:
    np_x = np.transpose(np_x)
if tr_b:
    np_y = np.transpose(np_y)

np_ans = np.matrix(np_x) * np.matrix(np_y)
self.assertShapeEqual(np_ans, tf_ans)
self.assertAllCloseAccordingToType(np_ans, out, rtol=1e-4, atol=1e-4)
