class MockEvaluator: # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.compat.v1.Session() as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
 # pragma: no cover
ops = type('MockOps', (object,), { # pragma: no cover
    'control_dependencies': staticmethod(lambda deps: tf.control_dependencies(deps))})() # pragma: no cover
 # pragma: no cover
self = MockEvaluator() # pragma: no cover

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
