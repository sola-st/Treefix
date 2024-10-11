device = 'CPU' # pragma: no cover
communication = 'RING' # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertAllClose = lambda a, b, rtol, atol: print('Comparing:', a, 'to', b) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
from l3.Runtime import _l_
group_size = 2
_l_(7235)
group_key = 101
_l_(7236)

dev0 = '/device:%s:0' % device
_l_(7237)
dev1 = '/device:%s:1' % device
_l_(7238)

@def_function.function
def run_all_reduce_2devices():
    _l_(7247)

    collectives = []
    _l_(7239)
    with ops.device(dev0):
        _l_(7242)

        group_handle0 = _collective_ops.initialize_communicator(
            group_key=group_key,
            rank=0,
            group_size=group_size,
            communication_hint=communication)
        _l_(7240)
        collectives.append(
            _collective_ops.all_reduce_v3(
                group_handle0, [1.0], reduction='Add'))
        _l_(7241)
    with ops.device(dev1):
        _l_(7245)

        group_handle1 = _collective_ops.initialize_communicator(
            group_key=group_key,
            rank=1,
            group_size=group_size,
            communication_hint=communication)
        _l_(7243)
        collectives.append(
            _collective_ops.all_reduce_v3(
                group_handle1, [2.0], reduction='Add'))
        _l_(7244)
    aux = collectives
    _l_(7246)
    exit(aux)

for result in run_all_reduce_2devices():
    _l_(7249)

    self.assertAllClose(result, [3.], rtol=1e-5, atol=1e-5)
    _l_(7248)
