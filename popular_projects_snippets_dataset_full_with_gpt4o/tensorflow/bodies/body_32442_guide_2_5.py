class MockEvaluate: # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.compat.v1.Session() as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
self = MockEvaluate() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
larry = constant_op.constant([])
_l_(21904)
curly = constant_op.constant([])
_l_(21905)
with ops.control_dependencies([check_ops.assert_near(larry, curly)]):
    _l_(21907)

    out = array_ops.identity(larry)
    _l_(21906)
self.evaluate(out)
_l_(21908)
