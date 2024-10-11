import unittest # pragma: no cover

Mock = type('Mock', (object,), {'assertRaisesOpError': unittest.TestCase.assertRaisesRegex, 'evaluate': staticmethod(lambda x: x)}) # pragma: no cover
self = Mock() # pragma: no cover

import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = unittest.TestCase() # pragma: no cover
self.assertRaisesOpError = lambda expected_err, msg: self.assertRaisesRegex(expected_err, msg) # pragma: no cover
self.evaluate = lambda op: exec('raise tf.errors.CancelledError(None, None, "was cancelled")') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
