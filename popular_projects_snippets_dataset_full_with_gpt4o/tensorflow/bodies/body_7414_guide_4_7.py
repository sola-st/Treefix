import portpicker # pragma: no cover
import re # pragma: no cover

class GrpcServerMock: # pragma: no cover
    def __init__(self, address): # pragma: no cover
        self.address = address # pragma: no cover
    def register(self, name, func): # pragma: no cover
        if name == 'assign' and not hasattr(func, 'input_signature'): # pragma: no cover
            raise ValueError('Input signature not specified for the function.') # pragma: no cover
mocked_GrpcServer = GrpcServerMock # pragma: no cover
rpc_ops = type('rpc_ops', (object,), {'GrpcServer': mocked_GrpcServer}) # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaisesRegex(self, exception, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self_): # pragma: no cover
                return self_ # pragma: no cover
            def __exit__(self_, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is None or not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f'Expected {exception}, got {exc_type}') # pragma: no cover
                if not re.search(regex, str(exc_value)): # pragma: no cover
                    raise AssertionError(f'Exception message does not match regex: {regex}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
from l3.Runtime import _l_
v = variables.Variable(initial_value=0, dtype=dtypes.int64)
_l_(21481)

@eager_def_function.function
def assign(a):
    _l_(21483)

    v.assign(a)
    _l_(21482)

port = portpicker.pick_unused_port()
_l_(21484)
address = "localhost:{}".format(port)
_l_(21485)
server = rpc_ops.GrpcServer(address)
_l_(21486)
with self.assertRaisesRegex(
    ValueError, "Input signature not specified for the function."):
    _l_(21488)

    server.register("assign", assign)
    _l_(21487)

# Register without input signature should work for functions without input
# args.
@eager_def_function.function
def read_var():
    _l_(21490)

    aux = v.value()
    _l_(21489)
    exit(aux)

server.register("read_var", read_var)
_l_(21491)
