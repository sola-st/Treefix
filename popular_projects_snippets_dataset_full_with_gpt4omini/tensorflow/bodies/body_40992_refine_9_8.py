import numpy as np # pragma: no cover

x = np.array([2.0, 3.0, 4.0]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
from l3.Runtime import _l_
aux = control_flow_ops.cond(
    math_ops.reduce_all(x > 1), lambda: 1. / x, lambda: x)
_l_(9539)
exit(aux)
