# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if gpu and self.gpu_backend is None:
    raise unittest.SkipTest("Test not running with GPU support")
backend = self.gpu_backend if gpu else self.cpu_backend
if dtype == np.bool_:
    x = np.random.randint(0, 2, size=shape).astype(np.bool_)
else:
    x = np.array(np.random.rand(*shape) * 100, dtype=dtype)
buffer = backend.buffer_from_pyval(x)
dlt = xla_client._xla.buffer_to_dlpack_managed_tensor(
    buffer, take_ownership=take_ownership)
del buffer  # Free "buffer" to make sure dlt retains ownership.
self.assertEqual(type(dlt).__name__, "PyCapsule")
y = xla_client._xla.dlpack_managed_tensor_to_buffer(
    dlt, self.cpu_backend, self.gpu_backend)
np.testing.assert_array_equal(
    x.astype(np.uint8) if dtype == np.bool_ else x, np.asarray(y))
