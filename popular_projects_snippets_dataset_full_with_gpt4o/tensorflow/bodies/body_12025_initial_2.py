from typing import List # pragma: no cover
import numpy as np # pragma: no cover

_ConcatGradHelper = type('Mock_ConcatGradHelper', (object,), {}) # pragma: no cover
class MockOp:# pragma: no cover
    def __init__(self, inputs):# pragma: no cover
        self.inputs = inputs# pragma: no cover
op = MockOp(inputs=[np.array([1, 2, 3]), np.array([4, 5, 6])]) # pragma: no cover
grad = np.array([1, 1, 1]) # pragma: no cover

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
