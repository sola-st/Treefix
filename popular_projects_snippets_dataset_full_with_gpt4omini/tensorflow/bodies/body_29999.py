# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
# Make sure zeros_like works even for dtypes that cannot be cast between
shape = (3, 5)
dtypes = np.float32, np.complex64
for in_type in dtypes:
    x = np.arange(15).astype(in_type).reshape(*shape)
    for out_type in dtypes:
        y = array_ops.zeros_like(x, dtype=out_type).numpy()
        self.assertEqual(y.dtype, out_type)
        self.assertEqual(y.shape, shape)
        self.assertAllEqual(y, np.zeros(shape, dtype=out_type))
