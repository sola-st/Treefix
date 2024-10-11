self = type('Mock', (object,), {'evaluate': lambda x: x})() # pragma: no cover

ops = type('Mock', (object,), {'control_dependencies': lambda self, deps: deps})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_near': lambda self, x, y: tf.debugging.assert_near(x, y)})() # pragma: no cover
array_ops = type('Mock', (object,), {'identity': lambda self, x: tf.identity(x)})() # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda self, x: x.numpy() if hasattr(x, 'numpy') else x})() # pragma: no cover

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
