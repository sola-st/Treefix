# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
# When extending `DeviceArrayBase`, the object behaves as a `DeviceArray`
# and thus needs to correctly implement the following methods.
arg = np.array([[1., 2., 3.]], np.float32)
buffer = self.backend.buffer_from_pyval(arg)
if not isinstance(buffer, xla_client.DeviceArrayBase):
    raise unittest.SkipTest(
        "The objectof type {} do not extend DeviceArrayBase".format(
            type(buffer)))

self.assertEqual(buffer.__array_priority__, 100)
self.assertEqual(buffer.shape, (1, 3))
self.assertEqual(buffer.dtype, np.float32)
self.assertEqual(buffer.size, 3)
self.assertEqual(buffer.ndim, 2)

self.assertIs(buffer, buffer.block_until_ready())
self.assertTrue(buffer.is_ready())
buffer.delete()
with self.assertRaises(xla_client.XlaRuntimeError):
    buffer.block_until_ready()
with self.assertRaises(xla_client.XlaRuntimeError):
    buffer.is_ready()
