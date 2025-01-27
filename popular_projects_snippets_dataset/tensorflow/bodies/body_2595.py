# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
arg0 = np.array([[1., 2.]], np.float32)
arg1 = np.array([[3., 4.]], np.float32)
arg0_buffer = self.backend.buffer_from_pyval(arg0)
arg1_buffer = self.backend.buffer_from_pyval(arg1)
# Prefetch two buffers using copy_to_host_async, and then retrieve their
# values using np.asarray().
arg0_buffer.copy_to_host_async()
arg0_buffer.copy_to_host_async()  # Duplicate calls don't do anything.
arg1_buffer.copy_to_host_async()
np.testing.assert_equal(arg0, np.asarray(arg0_buffer))
np.testing.assert_equal(arg1, np.asarray(arg1_buffer))
# copy_to_host_async does nothing after np.asarray() is called.
arg0_buffer.copy_to_host_async()
np.testing.assert_equal(arg0, np.asarray(arg0_buffer))
