import types # pragma: no cover

class MockOp:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.outputs = 'Output Value'# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
from l3.Runtime import _l_
aux = self._op.outputs
_l_(5331)
exit(aux)
