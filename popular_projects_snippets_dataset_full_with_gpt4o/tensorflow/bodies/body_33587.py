# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
sign_tf, abs_log_det_tf = tf_ans
shape = matrix_x.shape
if shape[-1] == 0 or shape[-2] == 0:
    np_sign, np_ans = (1.0, np.zeros(shape[:-2]).astype(matrix_x.dtype))
else:
    np_sign, np_ans = np.linalg.slogdet(matrix_x)
    np_ans = np_ans.astype(matrix_x.dtype)

self.assertShapeEqual(np_ans, abs_log_det_tf)
sign_tf_val = self.evaluate(sign_tf)
abs_log_det_tf_val = self.evaluate(abs_log_det_tf)
self.assertAllClose(
    sign_tf_val * np.exp(abs_log_det_tf_val),
    np_sign * np.exp(np_ans),
    atol=5e-5)
