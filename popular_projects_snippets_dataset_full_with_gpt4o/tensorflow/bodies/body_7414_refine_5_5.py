import portpicker # pragma: no cover

portpicker = portpicker # pragma: no cover
rpc_ops = type('MockGrpcServer', (object,), {'GrpcServer': lambda self, address: type('MockServer', (object,), {'register': lambda self, name, func: None})}) # pragma: no cover

import portpicker # pragma: no cover
import unittest # pragma: no cover

rpc_ops = type('Mock', (object,), {'GrpcServer': lambda address: type('MockServer', (object,), {'register': lambda self, name, func: None})()})() # pragma: no cover
self = type('Mock', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex})() # pragma: no cover

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
