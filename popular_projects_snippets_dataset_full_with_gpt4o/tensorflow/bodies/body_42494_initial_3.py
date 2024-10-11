import unittest # pragma: no cover

RemoteWorkerMemoryTest = type('RemoteWorkerMemoryTest', (unittest.TestCase,), {}) # pragma: no cover
self = RemoteWorkerMemoryTest() # pragma: no cover
method = 'test_method' # pragma: no cover
server_lib = type('server_lib', (), {'Server': type('Server', (), {'create_local_server': lambda: type('MockServer', (), {'target': 'grpc://localhost'})()})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/remote_memory_test.py
from l3.Runtime import _l_
super(RemoteWorkerMemoryTest, self).__init__(method)
_l_(22259)

# used for remote worker tests
self._cached_server = server_lib.Server.create_local_server()
_l_(22260)
self._cached_server_target = self._cached_server.target[len("grpc://"):]
_l_(22261)
