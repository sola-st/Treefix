# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array(np.random.rand(3, 4, 5, 6), dtype=np.float32)
buffer = self.backend.buffer_from_pyval(x)
_ = xla_client._xla.buffer_to_dlpack_managed_tensor(
    buffer, take_ownership=True)
self.assertTrue(buffer.is_deleted())
with self.assertRaisesRegex(
    RuntimeError,
    "Cannot convert deleted/invalid buffer to DLPack tensor.*"):
    _ = xla_client._xla.buffer_to_dlpack_managed_tensor(
        buffer, take_ownership=True)
