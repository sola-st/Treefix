# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
for use_gpu in [True, False]:
    for value in [1., 1j, 1. + 1j]:
        with self.subTest(use_gpu=use_gpu, value=value):
            np_real, np_imag = np.real(value), np.imag(value)
            with test_util.device(use_gpu=use_gpu):
                tf_real = math_ops.real(value)
                tf_imag = math_ops.imag(value)
                self.assertAllEqual(np_real, self.evaluate(tf_real))
                self.assertAllEqual(np_imag, self.evaluate(tf_imag))
