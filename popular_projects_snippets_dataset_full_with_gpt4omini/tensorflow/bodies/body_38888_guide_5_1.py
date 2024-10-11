class Mock: # pragma: no cover
    def assertRaisesOpError(self, message): # pragma: no cover
        return self.assertRaises(OpError, lambda: self.evaluate(takeg_op), message) # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: (_ for _ in ()).throw(OpError('was cancelled')) # pragma: no cover
takeg_op = lambda: None  # This lambda represents a placeholder operation # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
