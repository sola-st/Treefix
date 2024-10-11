# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
x = np.array([[-2, 3, -1] * 64, [1, -3, -3] * 64] * 8192)  # [16384, 192]
c_mat = np.array([[False] * 192, [True] * 192] * 8192)  # [16384, 192]
c_vec = np.array([False, True] * 8192)  # [16384]
np_val = np.where(c_mat, x * x, -x)
with self.session():
    tf_val = array_ops.where(c_vec, x * x, -x).eval()
self.assertAllEqual(tf_val, np_val)
