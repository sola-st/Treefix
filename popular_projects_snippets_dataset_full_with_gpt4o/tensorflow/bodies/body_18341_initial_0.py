self = type('Mock', (object,), {'_op': type('Mock', (object,), {'outputs': 'mock_outputs'})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
from l3.Runtime import _l_
aux = self._op.outputs
_l_(16860)
exit(aux)
