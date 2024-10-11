import portpicker # pragma: no cover

rpc_ops = type('Mock', (object,), {'GrpcServer': lambda address: type('MockGrpcServer', (object,), {'register': lambda self, name, func: None})()}) # pragma: no cover
self = type('Mock', (object,), {'assertRaisesRegex': lambda *args, **kwargs: None})() # pragma: no cover

import portpicker # pragma: no cover
from unittest import mock # pragma: no cover

portpicker = type('MockPortPicker', (object,), {'pick_unused_port': staticmethod(lambda: 12345)})() # pragma: no cover
rpc_ops = type('MockRPC', (object,), {'GrpcServer': lambda address: type('MockServer', (object,), {'register': lambda self, name, func: None})()})() # pragma: no cover
self = mock.Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
from l3.Runtime import _l_
v = variables.Variable(initial_value=0, dtype=dtypes.int64)
_l_(8841)

@eager_def_function.function
def assign(a):
    _l_(8843)

    v.assign(a)
    _l_(8842)

port = portpicker.pick_unused_port()
_l_(8844)
address = "localhost:{}".format(port)
_l_(8845)
server = rpc_ops.GrpcServer(address)
_l_(8846)
with self.assertRaisesRegex(
    ValueError, "Input signature not specified for the function."):
    _l_(8848)

    server.register("assign", assign)
    _l_(8847)

# Register without input signature should work for functions without input
# args.
@eager_def_function.function
def read_var():
    _l_(8850)

    aux = v.value()
    _l_(8849)
    exit(aux)

server.register("read_var", read_var)
_l_(8851)
