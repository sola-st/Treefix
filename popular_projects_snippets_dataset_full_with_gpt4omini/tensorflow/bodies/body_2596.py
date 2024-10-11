# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.arange(8, dtype=np.int32)
for device in self.backend.local_devices():
    buf = self.backend.buffer_from_pyval(x, device=device)
    self.assertEqual(buf.device(), device)
    np.testing.assert_equal(x, np.asarray(buf))
