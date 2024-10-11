from typing import List # pragma: no cover
import numpy as np # pragma: no cover

_ConcatGradHelper = type('MockConcatGradHelper', (object,), {}) # pragma: no cover
op = type('MockOp', (object,), {'inputs': list(np.random.rand(5, 3))})() # pragma: no cover
grad = np.random.rand(5, 3) # pragma: no cover

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
