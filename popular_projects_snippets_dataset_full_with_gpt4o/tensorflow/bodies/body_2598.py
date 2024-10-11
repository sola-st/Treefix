# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if not isinstance(self.backend, xla_client.Client):
    self.skipTest("TPU Driver doesn't support UnsafeBufferPointer().")
arg0 = np.array([])
arg1 = np.array([[0., 1., 2.]], np.float32)
arg2 = np.array([[3., 4., 5.]], bfloat16)
arg0_buffer = self.backend.buffer_from_pyval(arg0)
arg1_buffer = self.backend.buffer_from_pyval(arg1)
arg2_buffer = self.backend.buffer_from_pyval(arg2)
self.assertGreaterEqual(arg0_buffer.unsafe_buffer_pointer(), 0)
self.assertGreaterEqual(arg1_buffer.unsafe_buffer_pointer(), 0)
self.assertGreaterEqual(arg2_buffer.unsafe_buffer_pointer(), 0)
