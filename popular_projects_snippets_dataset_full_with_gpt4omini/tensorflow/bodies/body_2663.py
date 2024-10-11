# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
lo, hi = 2., 4.
shape = (2, 3)
c = self._NewComputation()
ops.RngUniform(
    ops.Constant(c, NumpyArrayF32(lo)),
    ops.Constant(c, NumpyArrayF32(hi)),
    shape=xla_client.Shape.array_shape(xla_client.PrimitiveType.F32,
                                       shape))
result = xla_client.execute_with_python_values(
    self.backend.compile(c.build()), (), backend=self.backend)
# since the result is random, we just check shape, uniqueness, and range
self.assertLen(result, 1)
self.assertEqual(result[0].shape, shape)
self.assertLen(np.unique(result[0]), np.prod(shape))
self.assertTrue(np.all(lo <= result[0]))
self.assertTrue(np.all(result[0] < hi))
