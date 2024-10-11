# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
arg = np.array([[1., 2.]], np.float32)
buffer = self.backend.buffer_from_pyval(arg)
buffer.delete()
with self.assertRaisesRegex(
    RuntimeError,
    re.escape(
        "BlockHostUntilReady() called on deleted or donated buffer")):
    buffer.block_until_ready()
