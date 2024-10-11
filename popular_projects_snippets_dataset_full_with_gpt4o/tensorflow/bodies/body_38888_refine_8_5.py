import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return self.assertRaisesRegex(tf.errors.OpError, msg) # pragma: no cover
 # pragma: no cover
    def evaluate(self, op): # pragma: no cover
        with tf.compat.v1.Session() as sess: # pragma: no cover
            return sess.run(op) # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
