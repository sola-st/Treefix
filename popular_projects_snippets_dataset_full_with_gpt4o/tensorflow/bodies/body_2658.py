# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Tuple(c, [
    ops.Constant(c, np.int32(42)),
    ops.Constant(c, NumpyArrayF32([1.0, 2.0])),
    ops.Constant(c, NumpyArrayBool([True, False, False, True]))
])
result = xla_client.execute_with_python_values(
    self.backend.compile(c.build()), (), backend=self.backend)
self.assertLen(result, 3)
np.testing.assert_equal(result[0], 42)
np.testing.assert_allclose(result[1], [1.0, 2.0])
np.testing.assert_equal(result[2], [True, False, False, True])
