# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
arg = np.arange(12, dtype=np.int16).reshape(3, 4)
c = self._NewComputation()
ops.Parameter(c, 0, xla_client.shape_from_pyval(arg))

options = xla_client.CompileOptions()
options.num_replicas = 1
compiled_c = self.backend.compile(c.build(), compile_options=options)

sharded_buffer = xla_client.ShardedBuffer.create_sharded_buffer(
    [self.backend.buffer_from_pyval(arg)])

results = compiled_c.execute_sharded_on_local_devices([sharded_buffer])
self.assertLen(results, 1)
self.assertIsInstance(results[0], xla_client.ShardedBuffer)
results[0].block_until_ready()

results, _ = compiled_c.execute_sharded_on_local_devices_with_tokens(
    [sharded_buffer])
self.assertLen(results, 1)
self.assertIsInstance(results[0], xla_client.ShardedBuffer)
results[0].block_until_ready()
