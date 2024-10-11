# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if not isinstance(self.backend, xla_client.Client):
    self.skipTest("TPU Driver doesn't support OnDeviceSizeInBytes.")
arg0 = np.array([])
arg1 = np.array([[0., 1., 2.]], np.float32)
arg2 = np.array([[3., 4., 5.]], bfloat16)
arg0_buffer = self.backend.buffer_from_pyval(arg0)
arg1_buffer = self.backend.buffer_from_pyval(arg1)
arg2_buffer = self.backend.buffer_from_pyval(arg2)
self.assertEqual(arg0_buffer.on_device_size_in_bytes(), 0)
# OnDeviceSizeInBytes varies depending on the platform. Confirm there's
# a reasonable value.
self.assertGreater(arg1_buffer.on_device_size_in_bytes(), 0)
self.assertGreater(arg2_buffer.on_device_size_in_bytes(), 0)
