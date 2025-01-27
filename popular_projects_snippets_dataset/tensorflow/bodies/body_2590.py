# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
arg = np.array([[1., 2.]], np.float32)
arg_buffer = self.backend.buffer_from_pyval(arg)
arg_buffer.block_until_ready()
