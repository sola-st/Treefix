# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.random.randn(20, 10)
buffer = self.backend.buffer_from_pyval(x)
buffer_ptr = buffer.unsafe_buffer_pointer()
y = np.array(buffer, copy=False)
buffer.delete()
# It is still legal to access `y`; the array view must keep it alive.
np.testing.assert_array_equal(x, y)
self.assertEqual(y.__array_interface__["data"][0], buffer_ptr)
