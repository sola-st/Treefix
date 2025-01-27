# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Constant(c, np.array([2.5, 3.3, -1.2, 0.7], np.float32))
options = xla_client.CompileOptions()
options.num_replicas = 1
compiled_c = self.backend.compile(c.build(), compile_options=options)

results = compiled_c.execute_sharded_on_local_devices([])
self.assertLen(results, 1)
self.assertIsInstance(results[0], list)
self.assertLen(results[0], 1)
results[0][0].block_until_ready()
self.assertIsInstance(results[0][0], xla_client.Buffer)

results, _ = compiled_c.execute_sharded_on_local_devices_with_tokens([])
self.assertLen(results, 1)
self.assertIsInstance(results[0], list)
self.assertLen(results[0], 1)
results[0][0].block_until_ready()
self.assertIsInstance(results[0][0], xla_client.Buffer)
