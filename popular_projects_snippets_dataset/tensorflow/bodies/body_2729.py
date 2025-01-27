# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
with xla_client.tracebacks(enabled=True):
    tb = xla_client.Traceback.get_traceback()
    self.assertIsTracebackContaining(tb, "testTracebacks")

    # Tracebacks are not implemented on the TPU driver extension's variant
    # of buffers and executables.
    if not isinstance(self.backend, xla_client.Client):
        exit()

    buffer = self.backend.buffer_from_pyval(np.array(7, np.int32))
    self.assertIsTracebackContaining(buffer.traceback, "testTracebacks")

    b = xla_client.XlaBuilder("computation")
    ops.Add(ops.Constant(b, np.int32(1)), ops.Constant(b, np.int32(2)))
    e = self.backend.compile(b.build())
    self.assertIsTracebackContaining(e.traceback, "testTracebacks")
