from unittest import TestCase # pragma: no cover

from unittest import TestCase # pragma: no cover

class MockTest(TestCase): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return self.assertRaises(tf.errors.OpError, msg) # pragma: no cover
    def evaluate(self, x): # pragma: no cover
        return x.numpy() if tf.executing_eagerly() else self.session().run(x) # pragma: no cover
 # pragma: no cover
self = MockTest('assertRaisesOpError') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
