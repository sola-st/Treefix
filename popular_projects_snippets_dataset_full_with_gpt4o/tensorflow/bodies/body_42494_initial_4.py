RemoteWorkerMemoryTest = type('RemoteWorkerMemoryTest', (object,), {'__init__': lambda self, method: None}) # pragma: no cover
self = type('MockSelf', (object,), {'__init__': lambda self: None})() # pragma: no cover
method = 'mock_method' # pragma: no cover
server_lib = type('MockServerLib', (object,), {'Server': type('MockServer', (object,), {'create_local_server': lambda: type('LocalServer', (object,), {'target': 'grpc://localhost:12345'})()})}) # pragma: no cover
self._cached_server = server_lib.Server.create_local_server() # pragma: no cover
self._cached_server_target = self._cached_server.target[len('grpc://'):] # pragma: no cover

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
