import numpy as np # pragma: no cover

_ConcatGradHelper = lambda op, grad, start_value_index, end_value_index, dim_index: (op.inputs[0], grad) # pragma: no cover
class MockOp: inputs = [np.array([1, 2, 3]), np.array([4, 5, 6])] # pragma: no cover
op = MockOp() # pragma: no cover
grad = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
from l3.Runtime import _l_
aux = _ConcatGradHelper(
    op,
    grad,
    start_value_index=1,
    end_value_index=len(op.inputs),
    dim_index=0)
_l_(8145)
exit(aux)
