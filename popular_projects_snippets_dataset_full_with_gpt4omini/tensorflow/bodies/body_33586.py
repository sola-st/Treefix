# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
out = self.evaluate(tf_ans)
shape = matrix_x.shape
if shape[-1] == 0 and shape[-2] == 0:
    np_ans = np.ones(shape[:-2]).astype(matrix_x.dtype)
else:
    np_ans = np.array(np.linalg.det(matrix_x)).astype(matrix_x.dtype)
self.assertShapeEqual(np_ans, tf_ans)
self.assertAllClose(np_ans, out, atol=5e-5)
