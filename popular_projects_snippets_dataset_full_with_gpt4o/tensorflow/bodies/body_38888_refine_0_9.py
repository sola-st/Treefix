from unittest import TestCase # pragma: no cover

from unittest import TestCase, mock # pragma: no cover

class CustomTestCase(TestCase): # pragma: no cover
    def assertRaisesOpError(self, expected_message): # pragma: no cover
        return self.assertRaises(tf.errors.OpError, msg=expected_message) # pragma: no cover
 # pragma: no cover
    def evaluate(self, x): # pragma: no cover
        return x.numpy() # pragma: no cover
 # pragma: no cover
self = CustomTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
