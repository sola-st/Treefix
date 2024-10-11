class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover

def mock_evaluate(x): # pragma: no cover
    if x is takeg_op: # pragma: no cover
        raise tf.errors.CancelledError('was cancelled') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
