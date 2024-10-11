# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_real, np_imag = np.real(cplx), np.imag(cplx)
np_zeros = np_real * 0

with test_util.device(use_gpu=use_gpu):
    inx = ops.convert_to_tensor(cplx)
    tf_real = math_ops.real(inx)
    tf_imag = math_ops.imag(inx)
    tf_real_real = math_ops.real(tf_real)
    tf_imag_real = math_ops.imag(tf_real)
    self.assertAllEqual(np_real, self.evaluate(tf_real))
    self.assertAllEqual(np_imag, self.evaluate(tf_imag))
    self.assertAllEqual(np_real, self.evaluate(tf_real_real))
    self.assertAllEqual(np_zeros, self.evaluate(tf_imag_real))
