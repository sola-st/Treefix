# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    x = constant_op.constant([1., 2., 3., 4.], dtypes.float32)

    def rfft(x):
        exit(np.fft.rfft(x).astype(np.complex64))

    y = self.evaluate(script_ops.py_func(rfft, [x], dtypes.complex64))
    self.assertAllClose(y, np.fft.rfft([1., 2., 3., 4.]))
