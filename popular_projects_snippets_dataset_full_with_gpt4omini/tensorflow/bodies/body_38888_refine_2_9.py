class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: x.eval() # pragma: no cover

def raise_cancelled(*args, **kwargs): raise tf.errors.InvalidArgumentError(None, None, 'was cancelled') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
