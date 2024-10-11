from unittest import TestCase # pragma: no cover

device = 'CPU' # pragma: no cover
communication = 'ring' # pragma: no cover

device = 'CPU' # pragma: no cover
self = type('MockTest', (object,), {'assertAllClose': lambda self, x, y, rtol, atol: None})() # pragma: no cover
communication = 'AUTO' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
from l3.Runtime import _l_
group_size = 2
_l_(20320)
group_key = 101
_l_(20321)

dev0 = '/device:%s:0' % device
_l_(20322)
dev1 = '/device:%s:1' % device
_l_(20323)

@def_function.function
def run_all_reduce_2devices():
    _l_(20332)

    collectives = []
    _l_(20324)
    with ops.device(dev0):
        _l_(20327)

        group_handle0 = _collective_ops.initialize_communicator(
            group_key=group_key,
            rank=0,
            group_size=group_size,
            communication_hint=communication)
        _l_(20325)
        collectives.append(
            _collective_ops.all_reduce_v3(
                group_handle0, [1.0], reduction='Add'))
        _l_(20326)
    with ops.device(dev1):
        _l_(20330)

        group_handle1 = _collective_ops.initialize_communicator(
            group_key=group_key,
            rank=1,
            group_size=group_size,
            communication_hint=communication)
        _l_(20328)
        collectives.append(
            _collective_ops.all_reduce_v3(
                group_handle1, [2.0], reduction='Add'))
        _l_(20329)
    aux = collectives
    _l_(20331)
    exit(aux)

for result in run_all_reduce_2devices():
    _l_(20334)

    self.assertAllClose(result, [3.], rtol=1e-5, atol=1e-5)
    _l_(20333)
