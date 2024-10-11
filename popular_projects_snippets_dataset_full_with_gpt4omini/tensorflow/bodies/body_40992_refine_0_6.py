import numpy as np # pragma: no cover

x = np.array([2, 3, 4]) # pragma: no cover

import numpy as np # pragma: no cover

class MockControlFlowOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def cond(pred, true_fn, false_fn):# pragma: no cover
        return true_fn() if pred() else false_fn() # pragma: no cover
class MockMathOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def reduce_all(x):# pragma: no cover
        return np.all(x) # pragma: no cover
control_flow_ops = MockControlFlowOps() # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
x = np.array([2, 3, 4]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
from l3.Runtime import _l_
aux = control_flow_ops.cond(
    math_ops.reduce_all(x > 1), lambda: 1. / x, lambda: x)
_l_(9539)
exit(aux)
