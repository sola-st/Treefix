# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Mul(
    ops.Constant(c, np.array([2.5, 3.3, -1.2, 0.7], np.float32)),
    ops.Constant(c, np.array([-1.2, 2, -2, -3], np.float32)))
num_replicas = 1
options = xla_client.CompileOptions()
options.num_replicas = num_replicas
compiled_c = self.backend.compile(c.build(), compile_options=options)
results, sharded_token = compiled_c.execute_sharded_on_local_devices_with_tokens(
    [])
sharded_token.block_until_ready()
self.assertLen(results, 1)
self.assertLen(results[0], 1)
np.testing.assert_allclose(
    np.asarray(results[0][0]),
    np.float32([-3, 6.6, 2.4, -2.1]),
    rtol=3e-3)
