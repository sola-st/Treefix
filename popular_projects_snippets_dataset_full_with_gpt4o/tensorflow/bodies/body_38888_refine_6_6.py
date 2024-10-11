import unittest # pragma: no cover

Mock = type('Mock', (object,), {'assertRaisesOpError': unittest.TestCase.assertRaisesRegex, 'evaluate': staticmethod(lambda x: x)}) # pragma: no cover
self = Mock() # pragma: no cover

import unittest # pragma: no cover

Mock = type('Mock', (object,), {'assertRaisesOpError': lambda self, expected_regex: self.assertRaises(tf.errors.CancelledError), 'evaluate': staticmethod(lambda x: (_ for _ in ()).throw(tf.errors.CancelledError(None, None, 'was cancelled')) if x is None else x)}) # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
