# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
np.random.seed(7)
with self.session(use_gpu=True):
    shape = [2]
    for dtype in [
        dtypes.quint8, dtypes.quint16, dtypes.qint8, dtypes.qint16,
        dtypes.qint32
    ]:
        with self.subTest(shape=shape, dtype=dtype):
            data = self.randn(shape, dtype.as_numpy_dtype)
            xs = list(map(constant_op.constant, data))
            c = math_ops.equal(array_ops.stack(xs), data)
            self.assertAllEqual(self.evaluate(c), [True, True])
