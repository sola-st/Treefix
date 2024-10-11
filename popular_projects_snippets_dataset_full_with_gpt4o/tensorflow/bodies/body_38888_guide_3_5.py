import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is None: # pragma: no cover
                    raise AssertionError('Expected OpError not raised') # pragma: no cover
                if isinstance(exc_value, tf.errors.CancelledError) and msg in str(exc_value): # pragma: no cover
                    return True # pragma: no cover
                raise exc_value # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
    def evaluate(self, op): # pragma: no cover
        raise tf.errors.CancelledError(None, None, 'was cancelled') # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover
takeg_op = 'mock_operation' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
