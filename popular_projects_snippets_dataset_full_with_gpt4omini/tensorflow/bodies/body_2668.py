# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
b = self._NewComputation("comparator")
p0 = ops.Parameter(b, 0, xla_client.shape_from_pyval(NumpyArrayF32(0)))
q0 = ops.Parameter(b, 1, xla_client.shape_from_pyval(NumpyArrayF32(0)))
p1 = ops.Parameter(b, 2, xla_client.shape_from_pyval(NumpyArrayS32(0)))
q1 = ops.Parameter(b, 3, xla_client.shape_from_pyval(NumpyArrayS32(0)))
ops.Or(ops.Lt(p0, q0), ops.And(ops.Eq(p0, q0), ops.Gt(p1, q1)))
comparator = b.build()

keys = np.array([[2, 3, 1, 3], [3, 1, 2, 2]], dtype=np.float32)
values = np.array([[0, 1, 2, 3], [4, 5, 6, 7]], dtype=np.int32)
c = self._NewComputation()
ops.Sort(
    c, (ops.Constant(c, keys), ops.Constant(c, values)),
    dimension=1,
    comparator=comparator)
result = xla_client.execute_with_python_values(
    self.backend.compile(c.build()), (), backend=self.backend)
self.assertLen(result, 2)
np.testing.assert_allclose(result[0], [[1, 2, 3, 3], [1, 2, 2, 3]])
np.testing.assert_equal(result[1], [[2, 0, 3, 1], [5, 7, 6, 4]])
