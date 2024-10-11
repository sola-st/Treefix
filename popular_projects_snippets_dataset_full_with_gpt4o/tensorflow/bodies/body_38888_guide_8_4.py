class Mock: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class Context: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is None: # pragma: no cover
                    raise AssertionError('Expected exception not raised') # pragma: no cover
                if not isinstance(exc_value, CancelledError): # pragma: no cover
                    raise AssertionError(f'Expected CancelledError but got {exc_type}') # pragma: no cover
                if msg not in str(exc_value): # pragma: no cover
                    raise AssertionError(f'Expected message "{msg}" but got "{str(exc_value)}"') # pragma: no cover
                return True # pragma: no cover
        return Context() # pragma: no cover
 # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        raise CancelledError(None, None, 'was cancelled') # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
