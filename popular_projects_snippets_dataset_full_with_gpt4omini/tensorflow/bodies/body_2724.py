# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array(np.random.rand(*shape) * 100, dtype=dtype)
x_ptr = x.__array_interface__["data"][0]
buffer = self.backend.buffer_from_pyval(
    x, host_buffer_semantics=xla_client.HostBufferSemantics.ZERO_COPY)
y = np.array(buffer, copy=False)
y_ptr = y.__array_interface__["data"][0]
np.testing.assert_array_equal(x, y)
# If the input was sufficiently aligned, the input and output should
# alias.
self.assertTrue((x_ptr & 15) != 0 or x_ptr == y_ptr)
self.assertEqual(y_ptr, buffer.unsafe_buffer_pointer())

during_call = xla_client.HostBufferSemantics.IMMUTABLE_ONLY_DURING_CALL
buffer2 = self.backend.buffer_from_pyval(
    x, host_buffer_semantics=during_call)
z = np.array(buffer2, copy=False)
self.assertNotEqual(x.__array_interface__["data"][0],
                    z.__array_interface__["data"][0])
