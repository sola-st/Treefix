# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
# TODO(b/185822300): re-enable after the bug is fixed in CUDA-11.x
# The input to svd should be a tensor of at least rank 2.
for bad_val in [np.nan, np.inf]:
    matrix = np.array([[1, bad_val], [0, 1]])
    s, u, v = linalg_ops.svd(matrix, compute_uv=True)
    s, u, v = self.evaluate([s, u, v])
    for i in range(2):
        self.assertTrue(np.isnan(s[i]))
        for j in range(2):
            self.assertTrue(np.isnan(u[i, j]))
            self.assertTrue(np.isnan(v[i, j]))
