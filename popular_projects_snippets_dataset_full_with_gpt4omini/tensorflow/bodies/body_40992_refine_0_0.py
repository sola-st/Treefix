import numpy as np # pragma: no cover

x = np.array([2, 3, 4]) # pragma: no cover

import numpy as np # pragma: no cover

class MockControlFlowOps: pass# pragma: no cover
control_flow_ops = MockControlFlowOps() # pragma: no cover
control_flow_ops.cond = lambda pred, true_fn, false_fn: true_fn() if pred() else false_fn() # pragma: no cover
class MockMathOps: pass# pragma: no cover
math_ops = MockMathOps() # pragma: no cover
math_ops.reduce_all = lambda x: all(x) # pragma: no cover
x = np.array([2, 3, 4]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
from l3.Runtime import _l_
aux = control_flow_ops.cond(
    math_ops.reduce_all(x > 1), lambda: 1. / x, lambda: x)
_l_(9539)
exit(aux)
