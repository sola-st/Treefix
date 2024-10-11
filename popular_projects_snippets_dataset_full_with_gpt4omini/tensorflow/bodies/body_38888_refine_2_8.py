class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: x.eval() # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
def assertRaisesOpError(func, *args, **kwargs): # pragma: no cover
    try: # pragma: no cover
        func(*args, **kwargs) # pragma: no cover
    except InvalidArgumentError as e: # pragma: no cover
        if 'was cancelled' in str(e): # pragma: no cover
            return # pragma: no cover
        raise # pragma: no cover
    raise AssertionError('Expected InvalidArgumentError was not raised') # pragma: no cover
self.assertRaisesOpError = assertRaisesOpError # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
