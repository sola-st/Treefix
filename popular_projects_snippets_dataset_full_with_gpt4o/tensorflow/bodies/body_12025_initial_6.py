from typing import Any # pragma: no cover

class _ConcatGradHelper:# pragma: no cover
    def __init__(self, op: Any, grad: Any, start_value_index: int, end_value_index: int, dim_index: int):# pragma: no cover
        self.op = op# pragma: no cover
        self.grad = grad# pragma: no cover
        self.start_value_index = start_value_index# pragma: no cover
        self.end_value_index = end_value_index# pragma: no cover
        self.dim_index = dim_index # pragma: no cover
op = type('MockOp', (object,), {'inputs': [1, 2, 3, 4]})() # pragma: no cover
grad = 'example_grad' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
from l3.Runtime import _l_
aux = _ConcatGradHelper(
    op,
    grad,
    start_value_index=1,
    end_value_index=len(op.inputs),
    dim_index=0)
_l_(20798)
exit(aux)
