class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: x() if callable(x) else x # pragma: no cover
self.assertRaisesOpError = lambda msg: (yield from self._assert_op_error(msg)) # pragma: no cover
def takeg_op(): raise OpError('was cancelled') # pragma: no cover
self._assert_op_error = lambda msg: (yield from self._mock_op_error(msg)) # pragma: no cover
def _mock_op_error(msg): raise OpError(msg) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
