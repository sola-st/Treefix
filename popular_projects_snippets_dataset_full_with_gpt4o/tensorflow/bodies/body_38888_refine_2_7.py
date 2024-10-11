import unittest # pragma: no cover

takeg_op = None # pragma: no cover
self = type('Mock', (object,), { 'assertRaisesOpError': unittest.TestCase.assertRaisesRegex, 'evaluate': lambda self, x: (_ for _ in ()).throw(Exception('was cancelled')) })() # pragma: no cover

import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), { 'assertRaisesOpError': lambda self, expected_regex: self.assertRaisesRegex(Exception, expected_regex), 'evaluate': lambda self, x: (_ for _ in ()).throw(Exception('was cancelled')) })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
