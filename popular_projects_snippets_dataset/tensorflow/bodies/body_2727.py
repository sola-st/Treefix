# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
with xla_client.tracebacks(enabled=False):
    self.assertEqual(None, xla_client.Traceback.get_traceback())
    buffer = self.backend.buffer_from_pyval(np.array(7, np.int32))
    self.assertEqual(None, buffer.traceback)

    b = xla_client.XlaBuilder("computation")
    ops.Add(ops.Constant(b, np.int32(1)), ops.Constant(b, np.int32(2)))
    e = self.backend.compile(b.build())
    self.assertEqual(None, e.traceback)
