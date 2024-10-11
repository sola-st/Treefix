# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Mul(
    ops.Constant(c, np.array([2.5, 3.3, -1.2, 0.7], np.float32)),
    ops.Constant(c, np.array([-1.2, 2, -2, -3], np.float32)))
compiled_c = self.backend.compile(c.build())
results, token = compiled_c.execute_with_token([])
token.block_until_ready()
self.assertLen(results, 1)
np.testing.assert_allclose(
    np.asarray(results[0]), np.float32([-3, 6.6, 2.4, -2.1]), rtol=3e-3)
