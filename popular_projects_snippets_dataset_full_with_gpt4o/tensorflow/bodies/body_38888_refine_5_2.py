import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('Mock', (object,), {'assertRaisesOpError': Mock(), 'evaluate': Mock()})() # pragma: no cover

import unittest # pragma: no cover

class CustomTestCase(unittest.TestCase): # pragma: no cover
    def assertRaisesOpError(self, expected_message): # pragma: no cover
        return self.assertRaisesRegex(tf.errors.OpError, expected_message) # pragma: no cover
 # pragma: no cover
    def evaluate(self, op): # pragma: no cover
        raise tf.errors.CancelledError(None, None, 'was cancelled') # pragma: no cover
 # pragma: no cover
self = CustomTestCase() # pragma: no cover
takeg_op = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
