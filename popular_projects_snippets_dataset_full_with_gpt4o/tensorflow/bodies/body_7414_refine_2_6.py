import portpicker # pragma: no cover
import pytest # pragma: no cover

rpc_ops = type('MockGrpc', (object,), {'GrpcServer': lambda address: type('MockServer', (object,), {'register': lambda self, name, func: None})()})() # pragma: no cover
self = type('MockSelf', (object,), {'assertRaisesRegex': lambda self, exception, regex: pytest.raises(exception, match=regex)})() # pragma: no cover

import portpicker # pragma: no cover

portpicker = portpicker # pragma: no cover
rpc_ops = type('MockGrpc', (object,), {'GrpcServer': lambda address: type('MockServer', (object,), {'register': lambda self, name, func: None})()})() # pragma: no cover
self = type('MockSelf', (object,), {'assertRaisesRegex': lambda self, exception, regex: type('ContextManager', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: isinstance(exc_val, exception) and bool(regex)})()})() # pragma: no cover

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
