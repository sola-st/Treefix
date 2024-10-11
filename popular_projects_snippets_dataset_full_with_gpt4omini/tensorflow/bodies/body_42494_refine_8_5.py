from unittest.mock import MagicMock # pragma: no cover

class RemoteWorkerMemoryTest: pass # pragma: no cover
self = MagicMock() # pragma: no cover
method = 'test_method' # pragma: no cover

class MockServer: pass # pragma: no cover

class RemoteWorkerMemoryTest(object): # pragma: no cover
    def __init__(self, method): # pragma: no cover
        self.method = method # pragma: no cover
        self._cached_server = ServerLibrary.create_local_server() # pragma: no cover
        self._cached_server_target = self._cached_server.__class__.__name__ # pragma: no cover
method = 'test_method' # pragma: no cover
ServerLibrary = type('ServerLibrary', (object,), {'create_local_server': staticmethod(lambda: MockServer())}) # pragma: no cover

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
