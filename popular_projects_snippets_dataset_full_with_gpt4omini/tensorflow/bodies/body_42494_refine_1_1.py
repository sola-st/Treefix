class RemoteWorkerMemoryTest(object): # pragma: no cover
    def __init__(self, method): # pragma: no cover
        self.method = method # pragma: no cover
        self._cached_server = server_lib.Server.create_local_server() # pragma: no cover
        self._cached_server_target = self._cached_server.target[len('grpc://'):] # pragma: no cover
        self._cached_server = type('MockServer', (object,), {'target': 'grpc://localhost:50051', 'create_local_server': classmethod(lambda cls: cls())})() # pragma: no cover
        self._cached_server_target = self._cached_server.target[len('grpc://'):] # pragma: no cover
method = 'test_method' # pragma: no cover
server_lib = type('Mock', (object,), {'Server': type('MockServer', (object,), {'create_local_server': classmethod(lambda cls: cls())})}) # pragma: no cover

class server_lib: pass # pragma: no cover

class RemoteWorkerMemoryTest(object): # pragma: no cover
    def __init__(self, method): # pragma: no cover
        self.method = method # pragma: no cover
        self._cached_server = self.create_mock_server() # pragma: no cover
        self._cached_server_target = self._cached_server.target[len('grpc://'):] # pragma: no cover
    def create_mock_server(self): # pragma: no cover
        return type('MockServer', (object,), {'target': 'grpc://localhost:50051', 'create_local_server': classmethod(lambda cls: cls())})() # pragma: no cover
 # pragma: no cover
method = 'test_method' # pragma: no cover
self = RemoteWorkerMemoryTest(method) # pragma: no cover
server_lib = type('Mock', (object,), {'Server': type('MockServer', (object,), {'create_local_server': classmethod(lambda cls: cls())})}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/remote_memory_test.py
from l3.Runtime import _l_
super(RemoteWorkerMemoryTest, self).__init__(method)
_l_(9868)

# used for remote worker tests
self._cached_server = server_lib.Server.create_local_server()
_l_(9869)
self._cached_server_target = self._cached_server.target[len("grpc://"):]
_l_(9870)
