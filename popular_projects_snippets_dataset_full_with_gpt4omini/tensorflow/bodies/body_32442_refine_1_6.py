ops = type('Mock', (object,), {'control_dependencies': lambda deps: deps})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_near': lambda x, y: None})() # pragma: no cover
array_ops = type('Mock', (object,), {'identity': lambda x: x})() # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda x: x})() # pragma: no cover

class Mock: # pragma: no cover
    def evaluate(self, out): # pragma: no cover
        return out# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover

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
