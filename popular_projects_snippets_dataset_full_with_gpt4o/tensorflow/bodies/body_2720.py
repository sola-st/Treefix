# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array(np.random.rand(3, 4, 5, 6), dtype=np.float32)
buffer = self.backend.buffer_from_pyval(x)
dlt = xla_client._xla.buffer_to_dlpack_managed_tensor(
    buffer, take_ownership=True)

def ConsumeDLPackTensor():
    _ = xla_client._xla.dlpack_managed_tensor_to_buffer(dlt, self.backend)

ConsumeDLPackTensor()
self.assertRaisesRegex(
    RuntimeError, ".*a DLPack tensor may be consumed at most once.*",
    ConsumeDLPackTensor)
