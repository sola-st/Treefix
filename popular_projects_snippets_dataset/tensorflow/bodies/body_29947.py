# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
np.random.seed(7)
with self.session():
    for shape in (2,), (3,), (2, 3), (3, 2), (8, 2, 10):
        for dtype in [np.complex64, np.complex128]:
            with self.subTest(shape=shape, dtype=dtype):
                data = self.randn(shape, dtype)
                xs = list(map(constant_op.constant, data))
                c = array_ops.stack(xs)
                self.assertAllEqual(self.evaluate(c), data)
