self = type('Mock', (object,), {'evaluate': lambda self, x: x})() # pragma: no cover

class Mock: pass # pragma: no cover
ops = Mock() # pragma: no cover
ops.control_dependencies = lambda deps: tf.control_dependencies(deps) # pragma: no cover
check_ops = Mock() # pragma: no cover
check_ops.assert_near = lambda x, y: tf.debugging.assert_near(x, y) # pragma: no cover
array_ops = Mock() # pragma: no cover
array_ops.identity = lambda x: tf.identity(x) # pragma: no cover
class Self: pass # pragma: no cover
self = Self() # pragma: no cover
self.evaluate = lambda x: x.numpy() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
larry = constant_op.constant([])
_l_(9580)
curly = constant_op.constant([])
_l_(9581)
with ops.control_dependencies([check_ops.assert_near(larry, curly)]):
    _l_(9583)

    out = array_ops.identity(larry)
    _l_(9582)
self.evaluate(out)
_l_(9584)
