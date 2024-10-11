import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
def mock_assertRaisesOpError(exception): # pragma: no cover
    class MockContext: pass # pragma: no cover
    context = MockContext() # pragma: no cover
    context.__enter__ = lambda: None # pragma: no cover
    context.__exit__ = lambda *args: args[0] == exception # pragma: no cover
    return context # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
