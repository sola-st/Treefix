# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
x = ops.Parameter(c, 0, xla_client.shape_from_pyval(NumpyArrayF32(2.0)))
result = ops.Add(x, ops.Constant(c, np.float32(3.14)))
ops.Add(result, ops.Constant(c, np.float32(1.618)))

arg = NumpyArrayF32(1.0)
compiled_c = self.backend.compile(c.build(result))
ans, = xla_client.execute_with_python_values(
    compiled_c, [arg], backend=self.backend)
np.testing.assert_allclose(ans, 4.14)
