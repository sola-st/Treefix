class MockClass(object): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
 # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is None: # pragma: no cover
                    raise AssertionError('OpError not raised') # pragma: no cover
                if not isinstance(exc_value, errors_impl.CancelledError): # pragma: no cover
                    raise AssertionError(f'Wrong exception type: {exc_value}') # pragma: no cover
                if msg not in str(exc_value): # pragma: no cover
                    raise AssertionError(f'Exception message not matched: {exc_value}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
    def evaluate(self, op): # pragma: no cover
        raise errors_impl.CancelledError(None, None, 'was cancelled') # pragma: no cover
 # pragma: no cover
self = MockClass() # pragma: no cover
takeg_op = 'mock_operation' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
