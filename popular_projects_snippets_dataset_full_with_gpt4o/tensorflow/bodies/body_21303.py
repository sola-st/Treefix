# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
# Starting a server with the same target as the cached server should fail.
server = self._cached_server
with self.assertRaises(errors_impl.UnknownError):
    _ = server_lib.Server(
        {"local_2": [server.target[len("grpc://"):]]})
