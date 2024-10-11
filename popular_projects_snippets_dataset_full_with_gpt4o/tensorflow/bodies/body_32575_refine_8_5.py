check_ops = type('Mock', (object,), {'assert_shapes': lambda shapes: tf.no_op()}) # pragma: no cover
ops = type('Mock', (object,), {'control_dependencies': lambda dependencies: tf.control_dependencies(dependencies)}) # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda x: x.eval()})() # pragma: no cover

self = type('Mock', (object,), {'evaluate': lambda self, x: tf.compat.v1.Session().run(x)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
x = array_ops.ones([1, 2, 3, 2], name="x")
_l_(20888)
y = array_ops.ones([2, 3, 3], name="y")
_l_(20889)
a1 = check_ops.assert_shapes([
    (x, (Ellipsis, "N", "Q")),
    (y, (Ellipsis, "N", "D")),
])
_l_(20890)
a2 = check_ops.assert_shapes([
    (x, "*NQ"),
    (y, "*ND"),
])
_l_(20891)
with ops.control_dependencies([a1, a2]):
    _l_(20893)

    out = array_ops.identity(x)
    _l_(20892)
self.evaluate(out)
_l_(20894)
