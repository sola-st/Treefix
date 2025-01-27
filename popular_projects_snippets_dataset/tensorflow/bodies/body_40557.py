# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
scalar_shape = constant_op.constant([], dtype=dtypes.int32)

x = random_ops.random_uniform(scalar_shape)
self.assertEqual(0, x.shape.ndims)
self.assertEqual(dtypes.float32, x.dtype)

x = random_ops.random_uniform(
    scalar_shape, minval=constant_op.constant(5.),
    maxval=constant_op.constant(6.))
self.assertLess(x, 6)
self.assertGreaterEqual(x, 5)
