import unittest # pragma: no cover

self = type('MockSelf', (object,), {'assertRaisesOpError': unittest.TestCase.assertRaises, 'evaluate': lambda x: (_ for _ in ()).throw(CustomError('was cancelled'))})() # pragma: no cover
takeg_op = lambda: 1 + 2  # This can be any valid operation # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
