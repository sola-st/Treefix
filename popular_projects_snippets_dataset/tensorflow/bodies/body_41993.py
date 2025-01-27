# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
# used for remote benchmarks
self._cached_server1 = server_lib.Server.create_local_server()
self._cached_server_target1 = self._cached_server1.target[len("grpc://"):]
self._cached_server2 = server_lib.Server.create_local_server()
self._cached_server_target2 = self._cached_server2.target[len("grpc://"):]
