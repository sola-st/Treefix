# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array(np.random.rand(3, 4, 5, 6), dtype=np.float32)
buffer = self.backend.buffer_from_pyval(x)
d1 = xla_client._xla.buffer_to_dlpack_managed_tensor(
    buffer, take_ownership=False)
d2 = xla_client._xla.buffer_to_dlpack_managed_tensor(
    buffer, take_ownership=False)

y = xla_client._xla.dlpack_managed_tensor_to_buffer(d1, self.backend)
z = xla_client._xla.dlpack_managed_tensor_to_buffer(d2, self.backend)
del d1, d2
np.testing.assert_array_equal(x, np.asarray(buffer))
np.testing.assert_array_equal(x, np.asarray(y))
np.testing.assert_array_equal(x, np.asarray(z))
