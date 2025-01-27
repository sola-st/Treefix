# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
arg = np.arange(12, dtype=np.int16).reshape(3, 4)
c = self._NewComputation()
ops.Parameter(c, 0, xla_client.shape_from_pyval(arg))

options = xla_client.CompileOptions()
options.num_replicas = 1
compiled_c = self.backend.compile(c.build(), compile_options=options)

buffer = self.backend.buffer_from_pyval(arg)

results = compiled_c.execute_sharded_on_local_devices([[buffer]])
self.assertLen(results, 1)
self.assertIsInstance(results[0], list)
self.assertLen(results[0], 1)
results[0][0].block_until_ready()
self.assertIsInstance(results[0][0], xla_client.Buffer)

results, _ = compiled_c.execute_sharded_on_local_devices_with_tokens(
    [[buffer]])
self.assertLen(results, 1)
self.assertIsInstance(results[0], list)
self.assertLen(results[0], 1)
results[0][0].block_until_ready()
self.assertIsInstance(results[0][0], xla_client.Buffer)
