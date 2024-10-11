import portpicker # pragma: no cover
import unittest # pragma: no cover

class MockSelf(unittest.TestCase): # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type: # pragma: no cover
                    raise AssertionError(f'Exception not raised') # pragma: no cover
                if not issubclass(exc_type, expected_exception): # pragma: no cover
                    raise AssertionError(f'Wrong exception type: {exc_type}') # pragma: no cover
                if not re.search(expected_regex, str(exc_value)): # pragma: no cover
                    raise AssertionError(f'Exception message does not match: {expected_regex}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
self = MockSelf('runTest') # pragma: no cover

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
