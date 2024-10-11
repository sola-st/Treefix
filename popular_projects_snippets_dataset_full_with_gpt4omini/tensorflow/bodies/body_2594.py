# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if not isinstance(self.backend, xla_client.Client):
    self.skipTest("TPU Driver doesn't support LiveBuffers().")
self.assertEmpty(self.backend.live_buffers())
arg0 = np.array([])
arg1 = np.array([[0., 1., 2.]], np.float32)
arg2 = np.array([[3., 4., 5.]], bfloat16)
arg0_buffer = self.backend.buffer_from_pyval(arg0)
arg1_buffer = self.backend.buffer_from_pyval(arg1)
arg2_buffer = self.backend.buffer_from_pyval(arg2)
self.assertLen(self.backend.live_buffers(), 3)
self.assertIs(self.backend.live_buffers()[0], arg2_buffer)
self.assertIs(self.backend.live_buffers()[1], arg1_buffer)
self.assertIs(self.backend.live_buffers()[2], arg0_buffer)
self.assertEqual(self.backend.devices()[0].live_buffers(),
                 self.backend.live_buffers())

arg1_buffer.delete()
self.assertLen(self.backend.live_buffers(), 2)
self.assertIs(self.backend.live_buffers()[0], arg2_buffer)
self.assertIs(self.backend.live_buffers()[1], arg0_buffer)

arg0_buffer.delete()
arg2_buffer.delete()
self.assertEmpty(self.backend.live_buffers())
