import numpy as np # pragma: no cover

class MockControlFlowOps(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def cond(pred, true_fn, false_fn, name=None): # pragma: no cover
        return tf.cond(pred, true_fn, false_fn, name) # pragma: no cover
 # pragma: no cover
class MockMathOps(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def reduce_all(input_tensor, axis=None, keepdims=False, name=None): # pragma: no cover
        return tf.reduce_all(input_tensor, axis, keepdims, name) # pragma: no cover
 # pragma: no cover
control_flow_ops = MockControlFlowOps # pragma: no cover
math_ops = MockMathOps # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
from l3.Runtime import _l_
aux = control_flow_ops.cond(
    math_ops.reduce_all(x > 1), lambda: 1. / x, lambda: x)
_l_(21903)
exit(aux)
