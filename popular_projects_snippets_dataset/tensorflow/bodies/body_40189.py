# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
super(RemoteExecutionTest, self).__init__(methodName)
self._cached_server1 = server_lib.Server.create_local_server()
self._cached_server2 = server_lib.Server.create_local_server()

self._cached_server1_target = self._cached_server1.target[len("grpc://"):]
self._cached_server2_target = self._cached_server2.target[len("grpc://"):]
