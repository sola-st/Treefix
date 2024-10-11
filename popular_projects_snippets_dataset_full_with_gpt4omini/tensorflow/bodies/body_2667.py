# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
keys = np.array([[2, 4, 1, 3], [3, 1, 4, 2]], dtype=np.float32)
values = np.array([[0, 1, 2, 3], [4, 5, 6, 7]], dtype=np.int32)
c = self._NewComputation()
ops.Sort(c, (ops.Constant(c, keys), ops.Constant(c, values)), dimension=0)
result = xla_client.execute_with_python_values(
    self.backend.compile(c.build()), (), backend=self.backend)
self.assertLen(result, 2)
np.testing.assert_allclose(result[0], [[2, 1, 1, 2], [3, 4, 4, 3]])
np.testing.assert_equal(result[1], [[0, 5, 2, 7], [4, 1, 6, 3]])
