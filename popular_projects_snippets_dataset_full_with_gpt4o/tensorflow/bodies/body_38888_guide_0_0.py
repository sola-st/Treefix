class MockEvaluator: # pragma: no cover
    def evaluate(self, op): # pragma: no cover
        raise errors.CancelledError(node_def=None, op=None, message='was cancelled') # pragma: no cover
 # pragma: no cover
def MockAssertRaisesOpError(expected_message): # pragma: no cover
    class Context: # pragma: no cover
        def __enter__(self): # pragma: no cover
            return self # pragma: no cover
        def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
            if exc_type is None: # pragma: no cover
                raise AssertionError('Exception not raised') # pragma: no cover
            if expected_message not in str(exc_value): # pragma: no cover
                raise AssertionError(f'Exception message does not match. Expected: {expected_message}, Got: {str(exc_value)}') # pragma: no cover
            return True # pragma: no cover
    return Context() # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'assertRaisesOpError': staticmethod(MockAssertRaisesOpError) # pragma: no cover
})() # pragma: no cover
takeg_op = 'some_operation' # pragma: no cover
self.evaluate = MockEvaluator().evaluate # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
